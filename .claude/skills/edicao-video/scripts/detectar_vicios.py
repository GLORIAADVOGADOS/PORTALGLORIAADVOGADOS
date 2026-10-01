#!/usr/bin/env python3
"""Propõe trechos a remover a partir da transcrição palavra a palavra.

Uso:
  python3 detectar_vicios.py transcript.json [--saida remover.json] [--extras "tipo,assim"]

Detecta:
  - vícios de fala (ééé, hã, hum, né...) isolados
  - palavra repetida em sequência ("o o", "que que")
  - recomeço: os mesmos 2-4 primeiros termos repetidos em até 6 s (frase reiniciada;
    remove a tentativa anterior)

Gera uma PROPOSTA. O agente deve mostrar a lista ao usuário e só então
passar o JSON para cortar.py --remover. Não remove nada sozinho.
"""
import argparse
import json
import re

VICIOS = {"é", "éé", "ééé", "eh", "ehh", "hã", "ãh", "ã", "hum", "hmm", "uhm",
          "ah", "ahn", "né", "tá", "aham"}


def norm(t):
    return re.sub(r"[^\wà-ú]", "", t.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcricao")
    ap.add_argument("--saida", default="remover.json")
    ap.add_argument("--extras", default="", help="vícios extras separados por vírgula")
    a = ap.parse_args()

    with open(a.transcricao) as f:
        w = json.load(f)
    if isinstance(w, dict):
        w = w.get("words", [])
    vicios = VICIOS | {norm(x) for x in a.extras.split(",") if x.strip()}
    props = []

    for i, p in enumerate(w):
        n = norm(p["text"])
        alongado = re.fullmatch(r"é{2,}|e{2,}h*|eh+|h*u*m{2,}|hu+m+|ã+h*|a+h+n?|hã+", n)
        if alongado or n in vicios:
            # "né"/"tá" só contam se isolados por pausa (evita cortar uso legítimo)
            if n in {"né", "tá", "é"}:
                antes = p["start"] - w[i - 1]["end"] if i else 1
                depois = w[i + 1]["start"] - p["end"] if i + 1 < len(w) else 1
                if min(antes, depois) < 0.15:
                    continue
            props.append({"start": p["start"], "end": p["end"], "motivo": f"vício: {p['text']}"})
        elif i and n and n == norm(w[i - 1]["text"]):
            props.append({"start": w[i - 1]["start"], "end": w[i - 1]["end"],
                          "motivo": f"repetição: {p['text']}"})

    # recomeços de frase: em cada posição tenta o prefixo mais longo primeiro;
    # ao achar, pula para o ponto de retomada (não gera propostas sobrepostas)
    i = 0
    while i < len(w) - 2:
        achou = None
        for k in (4, 3, 2):
            if i + k > len(w):
                continue
            chave = [norm(x["text"]) for x in w[i:i + k]]
            for j in range(i + k, min(len(w) - k + 1, i + 40)):
                if w[j]["start"] - w[i]["start"] > 6:
                    break
                if [norm(x["text"]) for x in w[j:j + k]] == chave:
                    achou = j
                    break
            if achou:
                break
        if achou:
            props.append({"start": w[i]["start"], "end": w[achou]["start"] - 0.02,
                          "motivo": "recomeço: " + " ".join(x["text"] for x in w[i:achou])})
            i = achou
        else:
            i += 1

    # une propostas sobrepostas
    props.sort(key=lambda x: x["start"])
    final = []
    for p in props:
        if final and p["start"] <= final[-1]["end"]:
            if p["end"] > final[-1]["end"]:
                final[-1]["end"] = p["end"]
                final[-1]["motivo"] += " + " + p["motivo"]
            continue
        final.append(dict(p))

    with open(a.saida, "w") as f:
        json.dump(final, f, ensure_ascii=False, indent=1)
    for p in final:
        print(f"{p['start']:7.2f}-{p['end']:7.2f}  {p['motivo']}")
    print(f"\n{len(final)} proposta(s) -> {a.saida}")


if __name__ == "__main__":
    main()
