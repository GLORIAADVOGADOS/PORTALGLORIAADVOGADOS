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

## §8 Estilo nomeado: "Estilo dos melhores do Instagram"

Engenharia reversa de dois Reels de referência (60 s e 54 s, 9:16, 30 fps)
que se apresentam como editados com Claude. Ofereça este estilo pelo nome
quando o propósito for **conteúdo orgânico de alto impacto, anúncio ou
lançamento** com pessoa falando para a câmera. **É uma estrutura, não uma
paleta:** a cor de destaque vem da marca do usuário (pergunte primeiro).

### Princípio
**"A fala vira interface."** Cada substantivo relevante falado ganha uma
representação visual no instante em que é dito (app citado → ícone aparece;
"arquivo" → cartão de arquivo; "formatos" → molduras 4:5/9:16). O vídeo
parece estar sendo editado *ao vivo* dentro de um software.

### Medições das referências
| Métrica | Valor medido | Como aplicar |
|---|---|---|
| Silêncio entre falas | **zero** pausa > 0,25 s a −35 dB nos dois vídeos | Ritmo **Acelerado** (§4) ou mais: `--min-silencio 0.25 --respiro 0.05` |
| Mudança visual relevante | ~23 em 61 s → **1 a cada ~2,6 s** | Planeje um "beat" visual a cada 2–4 s |
| Capítulos do HUD | 9 capítulos em ~50 s → **1 a cada ~5,5 s** | Troca de cena/tema a cada 5–7 s |
| Loudness | **−14,1 LUFS**, LRA 1,7–2,2 LU (voz muito comprimida), pico −0,8 dBTP | `loudnorm=I=-14:TP=-1:LRA=3`; compressão forte na voz |
| Trilha e SFX | Presentes: o próprio HUD exibe faixas "Trilha sonora / Efeito sonoro". Confiança média (não houve escuta) | Trilha discreta (−20 a −24 dB sob a voz) + whoosh/pop em cada entrada de grafismo |

### Estrutura temporal (vídeo de ~60 s)
1. **0–3 s, gancho tipográfico:** título de 2 linhas no topo, caixa alta, sans *black*. Linha 1 em branco e menor; linha 2 com o **número ou palavra-chave gigante (~2× a linha 1)** na cor de destaque, com gradiente e brilho. O valor pode "contar" ou trocar (R$ 0 → R$ 4 MIL) e ganhar partículas temáticas. Variante: frase de choque em 3 linhas ("EU GRAVEI / ESSE VÍDEO / UMA VEZ SÓ"), com a última linha em destaque.
2. **3–50 s, corpo:** legenda progressiva (abaixo) + beats visuais a cada 2–4 s + HUD persistente.
3. **50–55 s, fechamento:** selo de status "EDIÇÃO CONCLUÍDA" com check verde (único uso de verde).
4. **55–60 s, CTA:** chamada em 2 palavras ("COMECE / HOJE", "COMENTA / EDIT PRO"), com a 2ª palavra gigante na cor de destaque + brilho. **End card** em fundo quase preto: nome do produto/marca em 2 linhas (linha 2 gigante em gradiente), botão pílula "Saiba mais ›" e chevrons animados apontando para baixo.

### Legenda (assinatura do estilo)
- **Acúmulo palavra a palavra:** blocos de 1–3 palavras; cada palavra *entra no momento em que é falada* (pop rápido, sem fade longo). **A palavra ativa fica na cor de destaque, as anteriores ficam em branco.** O bloco zera a cada 2–3 palavras ou na pausa de frase.
- Fonte sans geométrica **bold/extra-bold** (Montserrat 800, Poppins 700/800), caixa normal (não caixa alta), **sem caixa de fundo**, com sombra suave para leitura.
- Tamanho ≈ 60–70 px em 1080×1920.
- Posição padrão ≈ 72 % da altura, mas **a legenda se desloca** (para ~24 % ou para dentro de painéis) para não colidir com grafismos.
- **Some** durante beats visuais fortes (rastreamento de mão, transformações): o grafismo assume a narração.
- Fallback sem hyperframes: `legenda_ass.py --estilo karaoke --palavras 3 --posicao 0.72` (aproximação: não faz acúmulo nem desvio).

### Camada de HUD ("editando ao vivo")
- Topo esquerdo: pílula escura com ponto vermelho pulsando + "EDITANDO AO VIVO 00:20:15" (timecode correndo), em fonte **mono** pequena (JetBrains Mono, IBM Plex Mono).
- Topo direito: contador de capítulo ("02 EDITOR", "06 RASTREIO DE MÃO", "08 FORMATOS"), que muda a cada capítulo.
- Painéis escuros semitransparentes com borda fina e **brilho na cor de destaque**: waveform, gráfico de keyframes, barra de "tokens", log de terminal.
- **Tela de editor:** o vídeo encolhe para dentro de uma interface com linha do tempo (faixas VÍDEO / LEGENDA / TRILHA / SFX / MOTION, cursor de reprodução, contagem "26 trechos") e volta para tela cheia.

### Repertório de beats visuais (escolha conforme a fala)
| Beat | Gatilho na fala | Técnica |
|---|---|---|
| Ícone de app/marca surge e flutua | nome de ferramenta, produto ou empresa | `hyperframes-animation` (pop + float) |
| Cartão de arquivo com linha animada ligando ícones | "arquivo", "manda", "pluga" | HTML + SVG com traço desenhado |
| Selo carimbado ("100% PROFISSIONAL") | adjetivo de valor | stamp com rotação e escala |
| Esqueleto da mão + objeto preso à mão | "colocar", "arrastar", "segurar" | rastreamento de mão (MediaPipe) + overlay. **Caro: 1–2 por vídeo** |
| Rótulos de rastreamento facial ("OLHOS", "BOCA") | falar de detalhe, reconhecimento | detecção facial + caixas com label |
| Moldura de crop 4:5 / 9:16 e mosaico de miniaturas | "formatos", "Reels", "anúncio", "YouTube" | molduras animadas + cópias reduzidas do vídeo |
| Troca/recorte de fundo, texto atrás da pessoa | "fundo", "cenário", "atrás de mim" | matting (`embedded-captions` usa remove-background) |
| Comparativo antes/depois | promessa de transformação | variante B abaixo |

### Variante B: comparativo permanente
Fundo escuro neutro (#111–#191919). Dois quadros: **"Vídeo normal"** (menor,
atrás, à esquerda) e **"Vídeo editado"** (maior, à frente, borda com brilho),
cada um com uma etiqueta-pílula. Pílulas brancas fixas no topo com a
afirmação central e **CTA fixo na base o vídeo inteiro** ("Comenta 'X'").
Exige crop e redimensionamento das duas versões lado a lado.

### Paletas das referências (só como exemplo; use a cor da marca)
| Referência | Fundo/painéis | Destaque (gradiente) | Apoio |
|---|---|---|---|
| A, laranja | `#070501` quase preto | `#F06810` → `#F89840` com brilho | branco; verde só no "concluído" |
| B, violeta | `#111111`–`#191919` | `#C880E0` → `#E088A8` (lilás → rosa), sombra `#582878` | branco; luz ambiente violeta/magenta |

Regra: **1 cor de destaque + branco + quase preto.** Nada além disso, exceto o verde de status.

### Custo e honestidade
- É o estilo mais caro do repertório: ~15–25 beats + HUD + legenda acumulativa. Sempre faça a amostra de 8–10 s primeiro.
- Rastreamento de mão/rosto e troca de fundo dependem de modelos de visão computacional. Avise que podem exigir mais rodadas de ajuste e que o resultado varia com a iluminação.
- "Editado 100% por IA" nas referências é discurso de venda: houve, no mínimo, direção humana detalhada.

### Adaptação para nichos regulados (§6)
Mantenha a estrutura (HUD, legenda acumulativa, beats), mas troque:
- gancho com dinheiro, moedas ou "ganhei R$ X" → **gancho de dúvida ou risco** ("Você sabia que perde esse direito em 2 anos?");
- "comenta X para receber" → avalie se configura captação; prefira "salve" ou "compartilhe";
- selos de autoelogio ("100% PROFISSIONAL") → selos informativos ("PRAZO: 2 ANOS", "CF, ART. 7º, XXIX").
