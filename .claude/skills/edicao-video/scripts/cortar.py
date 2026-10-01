#!/usr/bin/env python3
"""Corta silêncios e/ou trechos marcados de um vídeo e remapeia a transcrição.

Uso:
  python3 cortar.py entrada.mp4 saida.mp4 [opções]

Opções:
  --ruido DB         limiar de silêncio em dB (padrão -35)
  --min-silencio S   duração mínima de silêncio para cortar, em s (padrão 0.45)
  --respiro S        margem mantida antes/depois de cada fala, em s (padrão 0.12)
  --min-trecho S     descarta trechos mantidos menores que isso (padrão 0.25)
  --remover ARQ      JSON com trechos extras a remover: [{"start": 3.2, "end": 5.1}, ...]
                     (ex.: erros, repetições, "ééé" identificados na transcrição)
  --sem-silencio     não detecta silêncio; corta apenas o que estiver em --remover
  --transcricao ARQ  transcript.json (lista de palavras {text,start,end}) para remapear
                     à nova linha do tempo -> grava <saida>.transcript.json
  --crf N            qualidade x264 (padrão 18)
  --simular          só calcula e imprime os trechos, sem renderizar

Saídas: o vídeo cortado, <saida>.edl.json (trechos mantidos) e, se houver,
<saida>.transcript.json com os tempos ajustados para as legendas.
"""
import argparse
import json
import re
import subprocess
import sys


def duracao(arq):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", arq],
        capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def tem_audio(arq):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
         "stream=index", "-of", "csv=p=0", arq],
        capture_output=True, text=True).stdout
    return bool(out.strip())


def detectar_silencios(arq, ruido, minimo):
    err = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", arq, "-vn",
         "-af", f"silencedetect=noise={ruido}dB:d={minimo}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    inicios = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    fins = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    total = duracao(arq)
    if len(fins) < len(inicios):  # silêncio até o fim do arquivo
        fins.append(total)
    return [(max(0.0, a), b) for a, b in zip(inicios, fins)]


def unir(trechos):
    trechos = sorted(trechos)
    res = []
    for a, b in trechos:
        if res and a <= res[-1][1]:
            res[-1] = (res[-1][0], max(res[-1][1], b))
        else:
            res.append((a, b))
    return res


def calcular_mantidos(total, silencios, manuais, respiro, min_trecho):
    # silêncios são encolhidos pelo respiro (margem natural na fala);
    # trechos manuais (erros, repetições) são removidos exatamente como marcados
    cortes = list(manuais)
    for a, b in silencios:
        a2 = a + respiro if a > 0 else 0.0
        b2 = b - respiro if b < total else total
        if b2 - a2 > 0.05:
            cortes.append((a2, b2))
    mantidos, t = [], 0.0
    for a, b in unir(cortes):
        if a - t >= min_trecho:  # descarta fragmentos que "piscam" na tela
            mantidos.append((t, a))
        t = b
    if total - t >= min_trecho:
        mantidos.append((t, total))
    return mantidos


def remapear(palavras, mantidos):
    saida, offset_novo = [], 0.0
    for a, b in mantidos:
        for p in palavras:
            meio = (p["start"] + p["end"]) / 2
            if a <= meio < b:
                q = dict(p)
                q["start"] = round(max(p["start"], a) - a + offset_novo, 3)
                q["end"] = round(min(p["end"], b) - a + offset_novo, 3)
                saida.append(q)
        offset_novo += b - a
    return saida


def renderizar(ent, sai, mantidos, crf, audio):
    partes, rotulos = [], []
    for i, (a, b) in enumerate(mantidos):
        partes.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}];")
        rot = f"[v{i}]"
        if audio:
            partes.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[a{i}];")
            rot += f"[a{i}]"
        rotulos.append(rot)
    n = len(mantidos)
    filtro = "".join(partes) + "".join(rotulos) + \
        f"concat=n={n}:v=1:a={1 if audio else 0}[v]" + ("[a]" if audio else "")
    script = sai + ".filtro.txt"
    with open(script, "w") as f:
        f.write(filtro)
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", ent,
           "-filter_complex_script", script, "-map", "[v]"]
    if audio:
        cmd += ["-map", "[a]", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(crf),
            "-pix_fmt", "yuv420p", "-movflags", "+faststart", sai]
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("saida")
    ap.add_argument("--ruido", type=float, default=-35)
    ap.add_argument("--min-silencio", type=float, default=0.45)
    ap.add_argument("--respiro", type=float, default=0.12)
    ap.add_argument("--min-trecho", type=float, default=0.25)
    ap.add_argument("--remover")
    ap.add_argument("--sem-silencio", action="store_true")
    ap.add_argument("--transcricao")
    ap.add_argument("--crf", type=int, default=18)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()

    total = duracao(a.entrada)
    audio = tem_audio(a.entrada)
    silencios, manuais = [], []
    if not a.sem_silencio:
        if not audio:
            sys.exit("Vídeo sem áudio: use --sem-silencio com --remover.")
        silencios = detectar_silencios(a.entrada, a.ruido, a.min_silencio)
    if a.remover:
        with open(a.remover) as f:
            manuais = [(float(x["start"]), float(x["end"])) for x in json.load(f)]

    mantidos = calcular_mantidos(total, silencios, manuais, a.respiro, a.min_trecho)
    if not mantidos:
        sys.exit("Nada restaria após os cortes; afrouxe --ruido ou --min-silencio.")
    novo = sum(b - x for x, b in mantidos)
    print(f"Original: {total:.2f}s | Final: {novo:.2f}s | "
          f"Removido: {total - novo:.2f}s ({(total - novo) / total:.0%}) | "
          f"Trechos mantidos: {len(mantidos)}")

    with open(a.saida + ".edl.json", "w") as f:
        json.dump([{"start": round(x, 3), "end": round(b, 3)} for x, b in mantidos], f, indent=1)

    if a.transcricao:
        with open(a.transcricao) as f:
            palavras = json.load(f)
        if isinstance(palavras, dict):  # tolera {"words": [...]}
            palavras = palavras.get("words", [])
        with open(a.saida + ".transcript.json", "w") as f:
            json.dump(remapear(palavras, mantidos), f, ensure_ascii=False, indent=1)

    if not a.simular:
        renderizar(a.entrada, a.saida, mantidos, a.crf, audio)
        print(f"OK -> {a.saida}")


if __name__ == "__main__":
    main()
