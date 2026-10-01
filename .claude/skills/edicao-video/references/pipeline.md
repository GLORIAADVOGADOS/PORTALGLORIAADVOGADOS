# Pipeline técnico

`SKILL_DIR` é a pasta desta skill. Os comandos assumem que você está na pasta de trabalho do projeto.

## §1 Pasta de trabalho

```
projeto/
  bruto/       # originais — nunca alterar
  trabalho/    # áudio, transcript, edl, amostras
  final/       # entregas
  fonts/       # .ttf/.otf das fontes escolhidas (para a legenda ASS)
  briefing.json
```

## §2 Requisitos

- `ffmpeg`/`ffprobe` (obrigatório), `python3` (scripts desta skill)
- Transcrição, uma das opções:
  1. `npx hyperframes transcribe bruto/video.mp4 -m large-v3 -l pt --json` (Whisper local). **Não use os modelos `.en` para português.** Se a CLI listar um modelo multilíngue menor, ele é mais rápido e menos preciso.
  2. `pip install faster-whisper` e depois o trecho Python abaixo (modelo `small` ou `medium` com `language="pt"`)
- Skills hyperframes (opcional): legendas avançadas, overlays e motion

```python
from faster_whisper import WhisperModel
import json
m = WhisperModel("medium", compute_type="int8")
segs, _ = m.transcribe("trabalho/audio.wav", language="pt", word_timestamps=True, vad_filter=False)
w = [{"text": x.word.strip(), "start": round(x.start, 3), "end": round(x.end, 3)} for s in segs for x in s.words]
json.dump(w, open("trabalho/transcript.json", "w"), ensure_ascii=False)
```

`vad_filter=False` mantém os vícios de fala na transcrição, que é o que a
detecção precisa encontrar. Revise nomes próprios e termos técnicos. O Whisper
erra siglas e nomes; corrija no JSON antes de gerar legendas.

## §3 Extrair áudio para transcrição

```bash
ffmpeg -i bruto/video.mp4 -vn -ac 1 -ar 16000 trabalho/audio.wav
```

## §4 Cortes

```bash
# 1) propostas de vícios, repetições e recomeços → mostrar ao usuário
python3 SKILL_DIR/scripts/detectar_vicios.py trabalho/transcript.json --saida trabalho/remover.json

# 2) simular com o ritmo escolhido (presets.md §4)
python3 SKILL_DIR/scripts/cortar.py bruto/video.mp4 trabalho/cortado.mp4 \
  --remover trabalho/remover.json --min-silencio 0.45 --respiro 0.12 --simular

# 3) renderizar e remapear a transcrição
python3 SKILL_DIR/scripts/cortar.py bruto/video.mp4 trabalho/cortado.mp4 \
  --remover trabalho/remover.json --min-silencio 0.45 --respiro 0.12 \
  --transcricao trabalho/transcript.json
# → trabalho/cortado.mp4, cortado.mp4.edl.json, cortado.mp4.transcript.json
```

Só erros manuais, sem cortar silêncio: `--sem-silencio --remover ...`.
Para revisar pontos de corte isolados, extraia um trecho:
`ffmpeg -ss 12 -t 6 -i trabalho/cortado.mp4 -c copy trabalho/check.mp4`.

### Reenquadrar (16:9 → 9:16)

```bash
# corte central
ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy out.mp4
# fundo desfocado + vídeo inteiro ao centro (quando o corte central perde informação)
ffmpeg -i in.mp4 -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:5[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" -c:a copy out.mp4
```

## §5 Legendas: fallback sem hyperframes

```bash
python3 SKILL_DIR/scripts/legenda_ass.py trabalho/cortado.mp4.transcript.json trabalho/legenda.ass \
  --fonte "Montserrat" --tamanho 72 --cor "#FFFFFF" --destaque "#FFD400" \
  --estilo karaoke --palavras 3 --posicao 0.72 --caixa-alta
ffmpeg -i trabalho/cortado.mp4 -vf "ass=trabalho/legenda.ass:fontsdir=fonts" -c:a copy trabalho/legendado.mp4
```

- Coloque o `.ttf` da fonte em `fonts/`. Sem ele, o libass troca por uma fonte padrão sem avisar. Confira na amostra.
- Em 9:16, `--posicao` entre 0.62 e 0.75 respeita as zonas seguras (presets.md §5).
- Para Discreta: `--estilo discreta --palavras 6 --tamanho 58 --posicao 0.78`.

## §6 Acabamento e exportação

Normalização de áudio (dupla passagem é mais precisa; uma passagem basta para redes):

```bash
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy -c:a aac -b:a 192k -ar 48000 out.mp4
```

| Destino | Resolução | fps | Vídeo | Áudio |
|---|---|---|---|---|
| Reels / TikTok / Shorts | 1080×1920 | 30 (ou o original) | H.264, CRF 18–20, yuv420p, `+faststart` | AAC 192k, 48 kHz, −14 LUFS |
| Feed 4:5 | 1080×1350 | 30 | idem | idem |
| YouTube 16:9 | 1920×1080 (ou 3840×2160) | original | H.264 CRF 18 | AAC 192–320k, −14 LUFS |
| WhatsApp | 720×1280, ≤ 16 MB se precisar | 30 | H.264 CRF 23–26 | AAC 128k |

Amostra rápida de 8 s a partir de um ponto representativo:
```bash
ffmpeg -ss 10 -t 8 -i trabalho/legendado.mp4 -c:v libx264 -crf 23 -preset veryfast -c:a aac trabalho/amostra.mp4
```

Miniatura para revisão visual sem abrir o vídeo:
```bash
ffmpeg -ss 3 -i trabalho/amostra.mp4 -frames:v 1 -vf scale=540:-1 trabalho/frame.png
```
Abra o frame (ferramenta de leitura de imagem) e confira legibilidade, zona
segura e fonte antes de mostrar ao usuário.
