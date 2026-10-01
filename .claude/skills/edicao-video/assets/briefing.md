# Briefing de edição

Envie as perguntas de uma vez só. Pule as que o pedido já respondeu. Onde
houver "sugira", ofereça 2 ou 3 opções de `references/presets.md` e recomende uma.

## A. Propósito e contexto
1. Qual o propósito? (anúncio · conteúdo orgânico · institucional · depoimento · tutorial · VSL · outro)
2. Onde será publicado? (Reels/TikTok/Shorts 9:16 · feed 4:5 · YouTube 16:9 · WhatsApp · site)
3. Duração-alvo? (sugira por propósito)
4. Público e tom? (sóbrio · didático · enérgico · emocional · premium)
5. É de profissão regulada? (advocacia, saúde, finanças...)

## B. Identidade
6. Já tem paleta de cores? (hex, manual de marca, logo, site, perfil de referência). Se não tiver, sugira.
7. Já usa fontes específicas? Tem os arquivos ou estão no Google Fonts? Se não, sugira.
8. Estilo de legenda: tem referência? Discreta ou de impacto? Se não souber, sugira.
9. Ritmo de corte: natural · dinâmico · acelerado? Se não souber, sugira.

## C. Material
10. Logo, imagens, B-roll, trilha. Os direitos de uso estão garantidos?
11. Algo que precisa sair ou entrar obrigatoriamente (CTA, aviso legal)?

---

## briefing.json (salvar após o "ok")

```json
{
  "proposito": "conteúdo orgânico",
  "plataforma": "reels",
  "formato": "1080x1920",
  "duracao_alvo_s": 60,
  "publico_tom": "empresários, sóbrio",
  "nicho_regulado": "advocacia",
  "paleta": {"fundo": "#0F1B2D", "texto": "#FFFFFF", "destaque": "#C9A227", "apoio": "#8A97A8"},
  "fontes": {"titulo": "Playfair Display", "legenda": "Lato"},
  "legenda": {"estilo": "palavra-chave", "caixa_alta": false, "palavras_por_bloco": 4, "posicao": 0.72},
  "ritmo": {"nome": "dinâmico", "min_silencio": 0.45, "respiro": 0.12, "ruido": -35},
  "extras": ["logo no fim", "CTA: link na bio"],
  "origem": {"paleta": "usuario|sugerida", "fontes": "usuario|sugerida"}
}
```

---

## Ficha de revisão (antes de entregar)

- [ ] Gancho nos primeiros 1–3 s
- [ ] Nenhum corte no meio de palavra (ouvir as junções)
- [ ] Nenhum "piscar" (trecho mantido curto demais)
- [ ] Legenda sincronizada do início ao fim (conferir o último minuto)
- [ ] Legenda dentro da zona segura, fonte correta e contraste suficiente
- [ ] Ortografia, nomes próprios e termos técnicos corretos na legenda
- [ ] Paleta e fontes conforme o briefing (nada inventado)
- [ ] Áudio normalizado, sem picos ou estouro
- [ ] Formato e resolução da plataforma
- [ ] Checklist de nicho regulado aplicado (se houver)
- [ ] CTA e avisos obrigatórios presentes
- [ ] Original preservado em `bruto/`
