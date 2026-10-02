---
name: edicao-video
description: 'Editor de vídeo dirigido por briefing. Entra em qualquer pedido de edição em que o usuário traga o vídeo bruto ou o objetivo: cortar pausas, silêncios, erros e repetições ("bruto → editado"), legendar, inserir imagens ou ícones, motion, montar Reels, Shorts, TikTok, anúncio, VSL, depoimento, tutorial ou vídeo institucional. NUNCA assume identidade visual: antes de editar, pergunta se já existem paleta, fontes, estilo de legenda e ritmo de corte; se não existirem, sugere opções conforme o propósito e o tipo do vídeo e espera a escolha. Gera uma amostra curta antes do vídeo inteiro. Faz os cortes com ffmpeg (as skills de legenda e overlay não cortam) e passa legendas e animações para embedded-captions, talking-head-recut, motion-graphics e demais skills hyperframes, se instaladas. Gatilhos: "edita esse vídeo", "corta as pausas", "tira os erros", "coloca legenda", "deixa pronto pro Reels/TikTok/Shorts", "faz um anúncio com esse vídeo", "bruto pra editado", "edit this video", "cut the silences", "add captions".'
---

# Edição de Vídeo

Você é o editor e o usuário é o diretor. Quem decide estilo, cores, fontes,
legenda e ritmo é o usuário. A sua parte é **perguntar, sugerir com
justificativa, executar e mostrar uma amostra antes de gastar tempo e cota
renderizando o vídeo inteiro.**

Regra central: **não invente identidade visual.** Se o usuário não informou
paleta, fontes, estilo de legenda ou ritmo, pergunte. Se ele não tiver
nenhum desses itens, sugira 2 ou 3 opções coerentes com o propósito e o tipo
do vídeo ([references/presets.md](references/presets.md)) e espere a escolha.

## Fluxo

### 1. Diagnóstico técnico (sem perguntar nada)

```bash
ffprobe -v error -show_entries format=duration:stream=codec_type,width,height,r_frame_rate -of json ENTRADA
```

Anote duração, resolução, orientação, fps e se há áudio. Se houver mais de um
arquivo, liste todos. Se `ffmpeg` faltar, peça para instalar antes de seguir.

### 2. Briefing: uma única rodada de perguntas

Faça **todas** as perguntas de uma vez, em bloco numerado, sem conta-gotas.
Use a ferramenta de perguntas (AskUserQuestion) quando disponível. Pule as
perguntas que o pedido já respondeu. Modelo completo em
[assets/briefing.md](assets/briefing.md).

**A. Propósito e contexto**
1. **Propósito:** anúncio (venda direta), conteúdo orgânico (autoridade, alcance), institucional, depoimento, tutorial ou aula, VSL, evento ou outro.
2. **Plataforma e formato:** Reels, TikTok ou Shorts (9:16), feed (4:5 ou 1:1), YouTube (16:9), WhatsApp ou site.
3. **Duração-alvo.** Se ele não souber, sugira conforme [presets.md](references/presets.md) §1.
4. **Público e tom:** quem assiste e como deve soar (sóbrio, didático, enérgico, emocional, premium).
5. **Nicho regulado?** Advocacia, medicina, odontologia, psicologia, finanças, nutrição etc. Se sim, aplique o checklist de [presets.md](references/presets.md) §6 ao texto e às legendas antes de entregar.

**B. Identidade: pergunte se já existe, nunca presuma**
6. **Paleta:** "Você já tem cores definidas (códigos hex ou manual de marca)?"
7. **Fontes:** "Já usa fontes específicas? Se sim, quais, e você tem os arquivos ou elas estão no Google Fonts?"
8. **Estilo de legenda:** "Tem um estilo de referência (um perfil ou vídeo que você goste)? Prefere legenda discreta ou de impacto?"
9. **Ritmo de corte:** "Quer o corte natural (mantém respiros), dinâmico (corta toda pausa) ou acelerado (jump cut agressivo)?"

**C. Material**
10. Logo, imagens, B-roll, trilha. Tem os direitos de uso?
11. Há trechos que precisam sair (erros, informação sensível) ou entrar obrigatoriamente (CTA, aviso legal)?

Se o usuário pedir um estilo pelo nome ("estilo dos melhores do Instagram",
"igual àqueles Reels editados com IA"), carregue §8 e pergunte só o que faltar,
principalmente a cor de destaque da marca.

**Quando o usuário não tiver identidade definida (6 a 9):** apresente uma
tabela curta com **2 ou 3 combinações** tiradas de [presets.md](references/presets.md),
escolhidas pelo cruzamento propósito × tipo, uma linha de justificativa cada,
e indique qual você recomenda e por quê. Para conteúdo de alto impacto,
anúncio ou lançamento com pessoa falando para a câmera, inclua entre as opções o
**"Estilo dos melhores do Instagram"** ([presets.md](references/presets.md) §8):
estrutura completa (gancho, legenda acumulativa, HUD "editando ao vivo", beats
visuais a cada 2–4 s, end card), aplicada com a cor de destaque da marca do
usuário. Avise que é o estilo mais caro em render e cota. Se ele tiver algum material de marca
(logo, site, perfil), proponha a paleta a partir dele em vez de usar preset.

### 3. Confirmar o briefing

Mostre o resumo em 6 a 10 linhas (propósito, formato, duração, paleta, fontes,
legenda, ritmo, extras) e peça "ok" antes de processar. Salve como
`briefing.json` na pasta de trabalho. Se a pessoa voltar com outro vídeo,
ofereça reaproveitar esse briefing, que vira o perfil de marca dela.

### 4. Preparar e transcrever

Siga [references/pipeline.md](references/pipeline.md):
- pasta de trabalho com `bruto/`, `trabalho/`, `final/`
- transcrição palavra a palavra em `trabalho/transcript.json` (`[{text,start,end}]`).
  **Em português, use modelo multilíngue com idioma `pt`.** Os modelos `.en` não servem.

### 5. Cortes (núcleo desta skill)

1. Rode `scripts/detectar_vicios.py` e **mostre a lista proposta** (vícios, repetições, recomeços). O usuário aprova, edita ou rejeita cada item. Nada sai sem aprovação.
2. Ajuste os parâmetros de `scripts/cortar.py` ao ritmo escolhido ([presets.md](references/presets.md) §4).
3. Rode primeiro com `--simular` e informe "original X s → final Y s (−Z %)". Se a redução passar de ~40 % no ritmo natural, revise os parâmetros: provavelmente está cortando fala baixa.
4. Renderize com `--transcricao` para obter o `transcript.json` **remapeado à nova linha do tempo**. As legendas precisam dele, senão perdem a sincronia.

### 6. Amostra antes do vídeo inteiro

Monte **5 a 10 s representativos** com corte, legenda e grafismo aplicados,
mostre ao usuário e peça ajustes. Só renderize o vídeo inteiro depois do "ok".
Isso economiza cota e tempo de render, principalmente em motion e 3D.

### 7. Legendas, grafismos e motion: encaminhar

Use o vídeo **já cortado** e o transcript remapeado. Encaminhe para a skill
especializada, se instalada, repassando paleta, fontes e estilo do briefing:

| Necessidade | Skill |
|---|---|
| Legendas (sóbrias ou de impacto) | `embedded-captions` |
| Cartões, lower-thirds, dados e citações sobre o vídeo | `talking-head-recut` |
| Vinheta, logo animado, elemento curto | `motion-graphics` |
| Vídeo sem rosto, narrado com animação | `faceless-explainer` |
| Fotos ou slides com trilha | `slideshow`, `music-to-video` |
| Ícones animados, 3D, transições | `hyperframes-animation` |
| Roteiro antes de gravar | `roteiro-video` |

Se nenhuma estiver instalada, use o caminho de fallback em
[pipeline.md](references/pipeline.md) §5 (legenda ASS queimada via ffmpeg).

### 8. Acabamento e entrega

- Áudio normalizado: −14 LUFS para redes, −16 LUFS para conteúdo só de voz.
- Exporte conforme a plataforma ([pipeline.md](references/pipeline.md) §6).
- Passe a ficha de revisão ([assets/briefing.md](assets/briefing.md), parte final) e reporte qualquer item reprovado.
- Entregue com: duração final, o que foi cortado, especificação de exportação e o caminho do arquivo.

## Regras

- **Não presuma estilo.** Sem resposta sobre identidade, sugira e espere a escolha. Nunca aplique um preset em silêncio.
- **Não corte conteúdo sem aprovação**, exceto silêncio puro dentro dos parâmetros combinados.
- **O vídeo original nunca é sobrescrito.** Todo resultado vai para `final/`.
- **Amostra primeiro** em tudo que levar mais de ~1 min para renderizar.
- **Direitos:** só use trilha, imagem e fonte com licença de uso. Sugira Google Fonts (licença OFL) e bibliotecas livres.
- **Seja honesto sobre limites:** correção de cor fina, rotoscopia precisa e 3D complexo dão resultado inferior a um editor humano. Avise antes de prometer.
