---
name: polo-revisar-peca
description: Revisa uma peça pronta da Pólo Soluções Elétricas (imagem, PDF ou arte de terceiros) contra o Guia Mestre e devolve o que está certo, o que ajustar e como corrigir. Use quando pedirem para conferir, revisar ou aprovar uma arte da Pólo.
---

# Revisão de peças da Pólo Soluções Elétricas

Referência: Guia Mestre da Identidade Visual v1
- No repositório: docs/02_GUIA_MESTRE_IDENTIDADE_VISUAL_v1
- Doc vivo: https://claude.ai/code/artifact/fb4897a3-9066-4ece-908f-ab10da5a5ab9

Regras de produção completas: skill polo-identidade-visual.

## Como revisar

1. Abra a peça e olhe inteira e em zoom (logo, títulos, rodapé, bordas).
2. Identifique o formato (post, story, carrossel, folheto, documento, apresentação, assinatura) e confira o tamanho.
3. Passe pelos 12 critérios abaixo, um por um. Julgue pelo que está visível, sem suposições.
4. Quando houver cor duvidosa, meça o HEX na imagem e compare com a paleta.
5. Entregue no formato de resposta abaixo.

## Critérios

| # | Critério | Passa quando |
| --- | --- | --- |
| 1 | Logo | É o logo neon oficial (setas vermelhas em tubo, PÓLO azul neon, descritor prateado), sem distorção, sem elementos sobrepostos, com área de proteção |
| 2 | Fundo do logo | Logo sobre fundo escuro; em peça clara, dentro de faixa/bloco Preto Pólo |
| 3 | Protagonismo | Logo Pólo visível e maior que qualquer logo de representada |
| 4 | Nome e dados | "Pólo Soluções Elétricas", "Desde 1987" (nunca "há X anos"), (49) 3328-4315, vendas@polorepres.com.br, @polo.repres |
| 5 | Paleta | Só #EE3016, #34086C, #06AFF9, #0B0B0F, #1A1A20, #FFFFFF, #0389F7, #E8E7EA, #6B7384, #2E2E35; vermelho em até ~10% da área; no escuro, um destaque quente e um frio |
| 6 | Tipografia | Montserrat, Barlow Condensed ExtraBold Itálico (títulos), Kaushan Script (no máx. 1 trecho); máx. 3 níveis de hierarquia |
| 7 | Estrutura | Três faixas: marca/título, conteúdo, base com representadas/CTA/contato |
| 8 | Margens e zonas | Margem lateral ≥ 6%; story com 250 px livres no topo e na base |
| 9 | Legibilidade | Nenhum texto cortado, sobreposto ou cruzado por linha; texto mínimo 24 px no feed; contraste adequado (nada de ciano sobre branco) |
| 10 | Grafismos | Linhas de energia em no máx. 2 cantos opostos; 1 moldura chanfrada; máx. 3 tarjas; ícones de linha, sem emojis |
| 11 | Imagens | Produto e pessoas em foto real; nada de banco de imagens genérico; IA só em fundo escurecido |
| 12 | Conteúdo | Densidade dentro do limite (40 palavras feed, 25 story, 5 itens por lista); potências no padrão "112,5 kVA \| 25 kV"; nenhum dado sem fonte |

## Formato da resposta

Primeira linha: veredito — APROVADA, APROVADA COM AJUSTES ou REFAZER.

Depois, uma tabela só com os critérios que não passaram:

| # | Problema encontrado | Correção |
| --- | --- | --- |

Feche com no máximo 2 linhas sobre o que está bem resolvido. Se a usuária pedir, aplique as correções usando a skill polo-identidade-visual e entregue a peça corrigida.
