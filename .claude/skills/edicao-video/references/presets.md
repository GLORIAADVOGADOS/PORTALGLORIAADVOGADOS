# Presets para sugestão

Use estas tabelas **só quando o usuário não tiver identidade definida**, ou
para complementar o que faltar. Sempre ofereça 2 ou 3 opções, recomende uma e
justifique em uma linha. Os valores são pontos de partida: ajuste após a amostra.

## §1 Duração-alvo por propósito

| Propósito | Duração sugerida | Por quê |
|---|---|---|
| Anúncio (venda direta) | 15–30 s (teste A/B com 3 ganchos diferentes) | A retenção cai rápido em tráfego frio; gancho nos primeiros 1–3 s |
| Conteúdo orgânico de autoridade | 30–90 s | Tempo para uma ideia completa sem perder retenção |
| Tutorial ou aula | 60 s–3 min (redes) ou 5–15 min (YouTube) | O passo a passo precisa de tempo; corte em capítulos |
| Depoimento | 30–60 s | Uma história, um resultado, uma emoção |
| Institucional | 45–90 s | Apresentação sem cansar |
| VSL | 3–15 min | Estrutura de venda longa (problema → solução → oferta) |

Limites de plataforma mudam com frequência. Confira o limite atual antes de
afirmar um número ao usuário.

## §2 Paletas por tom

Formato: fundo / texto / destaque / apoio. Verifique contraste ≥ 4.5:1 entre
texto e fundo da legenda.

| Tom | Paleta | Combina com |
|---|---|---|
| **Sóbrio e confiável** | `#0F1B2D` / `#FFFFFF` / `#C9A227` / `#8A97A8` | Advocacia, consultoria, finanças, institucional |
| **Clínico e limpo** | `#FFFFFF` / `#1D2939` / `#2E90FA` / `#D1E9FF` | Saúde, odontologia, tutorial |
| **Enérgico** | `#111111` / `#FFFFFF` / `#FFD400` / `#FF3B30` | Anúncio, oferta, conteúdo viral |
| **Premium** | `#0B0B0B` / `#F5F1E8` / `#B08D57` / `#3A3A3A` | Alto padrão, imobiliário, estética |
| **Acolhedor** | `#FFF8F0` / `#3D2C2E` / `#E07A5F` / `#81B29A` | Psicologia, família, bem-estar, depoimento |
| **Tecnológico** | `#0A0F1F` / `#E6EDF3` / `#7C5CFF` / `#22D3EE` | SaaS, IA, tutorial de software |

Se o usuário tiver logo ou site, extraia 2 ou 3 cores dele e monte a paleta
nesse formato. Isso vale mais do que qualquer preset.

## §3 Fontes (Google Fonts, licença OFL, uso comercial livre)

| Estilo | Título / destaque | Texto / legenda | Uso |
|---|---|---|---|
| Moderno neutro | Inter (800) | Inter (600) | Seguro para qualquer nicho |
| Impacto | Anton ou Bebas Neue | Montserrat (700) | Anúncio, gancho, palavra-chave |
| Elegante | Playfair Display (700) | Lato (700) | Premium, advocacia, institucional |
| Amigável | Poppins (800) | Poppins (600) | Educativo, saúde, família |
| Editorial | DM Serif Display | DM Sans (600) | Autoridade, opinião, citação |

Legenda: peso ≥ 600, nunca fina. Em 1080 px de largura, 56–80 px de corpo.

## §4 Ritmo de corte → parâmetros de `cortar.py`

| Ritmo | `--min-silencio` | `--respiro` | `--ruido` | Efeito |
|---|---|---|---|---|
| **Natural** | 0.70 | 0.18 | −35 | Mantém respiros; tom de conversa. Institucional, depoimento |
| **Dinâmico** (padrão de redes) | 0.45 | 0.12 | −35 | Sem pausas mortas, ainda humano. Orgânico, tutorial |
| **Acelerado** | 0.30 | 0.06 | −32 | Jump cut agressivo. Anúncio, gancho, viral |

Ajustes de ruído: gravação com ruído de fundo (ar-condicionado, rua) → suba
para −30/−28; gravação muito limpa e voz baixa → desça para −40.
Recomeço e vício de fala sempre via `detectar_vicios.py` com aprovação.

Complementos de ritmo (aplicados na composição, não no corte):
- **Zoom de ênfase** (punch-in de 110–120 %) a cada 5–10 s no ritmo dinâmico ou acelerado, para quebrar a monotonia do plano fixo.
- **B-roll ou imagem** a cada 8–15 s em conteúdo explicativo.
- **Gancho** (texto grande ou pergunta) nos primeiros 1–2 s em qualquer vídeo de rede social.

## §5 Estilos de legenda

| Estilo | Descrição | Quando usar | Quando evitar |
|---|---|---|---|
| **Discreta** | 1–2 linhas, terço inferior, ≤ 38 caracteres/linha, sem animação | Institucional, aula longa, nicho sóbrio | Anúncio em tráfego frio |
| **Palavra-chave em destaque** | Frase em branco, 1 palavra na cor de destaque | Autoridade, educativo (equilíbrio padrão) | — |
| **Karaokê** | 2–4 palavras por vez, a palavra falada acende | Redes sociais, retenção | Conteúdo muito sóbrio |
| **Impacto** | 1–3 palavras gigantes, centralizadas, com pop ou escala | Gancho, anúncio, frase de efeito | Vídeo inteiro (cansa) |
| **Editorial** | Serifada, caixa alta/baixa, fundo translúcido | Premium, citação, depoimento | Público jovem/viral |

Zonas seguras em 9:16 (1080×1920, aproximado; varia por app): mantenha o texto
fora dos ~250 px superiores, dos ~400 px inferiores e dos ~120 px à direita,
onde ficam a interface, a descrição e os botões.

Velocidade de leitura: no máximo ~17 caracteres/segundo. Acima disso, divida
a legenda em mais blocos.

## §6 Nichos regulados: checklist antes da entrega

Aplique ao **texto falado, às legendas e aos grafismos**. Se encontrar um
problema, aponte o trecho e sugira uma redação alternativa. Não remova
conteúdo sem aprovação. As normas mudam: confirme a versão vigente.

| Nicho | Norma de referência | Pontos de atenção |
|---|---|---|
| Advocacia | Provimento OAB 205/2021 e Código de Ética | Sem promessa de resultado, sem captação ou mercantilização, sem divulgar valores de honorários, sem autoengrandecimento ou ostentação; caráter informativo |
| Medicina | Resolução CFM 2.336/2023 | Sem garantia de resultado; regras específicas para antes/depois; identificação com CRM/RQE |
| Odontologia | Normas do CFO sobre publicidade | Antes/depois com regras; sem garantia de resultado; identificação com CRO |
| Finanças e investimentos | Normas CVM e ANBIMA | Sem promessa de rentabilidade; avisos de risco |
| Saúde em geral (psicologia, nutrição, estética) | Conselho profissional respectivo | Sem promessa de cura ou resultado; cuidado com depoimentos |
| Publicidade em geral | CDC (arts. 36–38) e Código CONAR | Publicidade identificável como tal; nada enganoso ou abusivo |

## §7 Matriz rápida: propósito × tipo → combinação recomendada

| Tipo \ Propósito | Anúncio | Orgânico / autoridade | Institucional / depoimento | Tutorial |
|---|---|---|---|---|
| **Pessoa falando para a câmera** | Enérgico + Impacto (fonte) + Karaokê + Acelerado | Tom do nicho + Moderno + Palavra-chave + Dinâmico | Sóbrio/Acolhedor + Elegante + Discreta/Editorial + Natural | Clínico + Amigável + Palavra-chave + Dinâmico |
| **Sem rosto (narração + animação)** | Enérgico + Impacto + Impacto (legenda) | Tecnológico/Clínico + Moderno + Karaokê | Premium + Editorial + Discreta | Clínico + Amigável + Discreta |
| **Gravação de tela** | — | Tecnológico + Moderno + Palavra-chave | — | Tecnológico + Moderno + Discreta + zoom no cursor |
| **Fotos ou slides com trilha** | Enérgico + Impacto | Premium/Acolhedor + Editorial | Acolhedor + Editorial | — |

"Tom do nicho" = a paleta de §2 que combina com o setor do usuário.
