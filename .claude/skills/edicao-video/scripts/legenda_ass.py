#!/usr/bin/env python3
"""Gera legenda .ass a partir do transcript (fallback sem hyperframes).

Uso:
  python3 legenda_ass.py transcript.json legenda.ass --largura 1080 --altura 1920 \
      --fonte "Montserrat" --tamanho 72 --cor "#FFFFFF" --destaque "#FFD400" \
      --estilo karaoke --palavras 3 --posicao 0.72 [--caixa-alta]

Estilos:
  discreta  blocos de até --palavras palavras, sem destaque
  karaoke   bloco fixo e a palavra falada na cor de destaque
Queimar:  ffmpeg -i video.mp4 -vf "ass=legenda.ass:fontsdir=fonts" -c:a copy saida.mp4
"""
import argparse
import json


def cor_ass(hexcor):
    h = hexcor.lstrip("#")
    r, g, b = h[0:2], h[2:4], h[4:6]
    return f"&H00{b}{g}{r}".upper()


def tempo(t):
    t = max(0.0, t)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def blocos(palavras, n, max_gap=0.6):
    atual = []
    for p in palavras:
        if atual and (len(atual) >= n or p["start"] - atual[-1]["end"] > max_gap
                      or atual[-1]["text"].rstrip().endswith((".", "?", "!"))):
            yield atual
            atual = []
        atual.append(p)
    if atual:
        yield atual


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcricao")
    ap.add_argument("saida")
    ap.add_argument("--largura", type=int, default=1080)
    ap.add_argument("--altura", type=int, default=1920)
    ap.add_argument("--fonte", default="Montserrat")
    ap.add_argument("--tamanho", type=int, default=72)
    ap.add_argument("--cor", default="#FFFFFF")
    ap.add_argument("--destaque", default="#FFD400")
    ap.add_argument("--contorno", default="#000000")
    ap.add_argument("--estilo", choices=["discreta", "karaoke"], default="karaoke")
    ap.add_argument("--palavras", type=int, default=3)
    ap.add_argument("--posicao", type=float, default=0.72,
                    help="altura do centro da legenda (0 = topo, 1 = base)")
    ap.add_argument("--caixa-alta", action="store_true")
    a = ap.parse_args()

    with open(a.transcricao) as f:
        w = json.load(f)
    if isinstance(w, dict):
        w = w.get("words", [])
    w = [p for p in w if p["text"].strip()]

    y = int(a.altura * a.posicao)
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {a.largura}
PlayResY: {a.altura}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Base,{a.fonte},{a.tamanho},{cor_ass(a.cor)},{cor_ass(a.destaque)},{cor_ass(a.contorno)},&H64000000,-1,0,0,0,100,100,0,0,1,{max(2, a.tamanho // 14)},2,5,80,80,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    linhas = []
    hl = cor_ass(a.destaque)
    base = cor_ass(a.cor)
    for bl in blocos(w, a.palavras):
        txt = [p["text"].strip() for p in bl]
        if a.caixa_alta:
            txt = [t.upper() for t in txt]
        pos = f"{{\\pos({a.largura // 2},{y})}}"
        if a.estilo == "discreta":
            linhas.append(f"Dialogue: 0,{tempo(bl[0]['start'])},{tempo(bl[-1]['end'])},Base,,0,0,0,,{pos}{' '.join(txt)}")
            continue
        for i, p in enumerate(bl):
            fim = bl[i + 1]["start"] if i + 1 < len(bl) else p["end"]
            partes = [(f"{{\\c{hl}}}{t}{{\\c{base}}}" if j == i else t) for j, t in enumerate(txt)]
            linhas.append(f"Dialogue: 0,{tempo(p['start'])},{tempo(fim)},Base,,0,0,0,,{pos}{' '.join(partes)}")

    with open(a.saida, "w", encoding="utf-8") as f:
        f.write(cab + "\n".join(linhas) + "\n")
    print(f"{len(linhas)} eventos -> {a.saida}")


if __name__ == "__main__":
    main()
