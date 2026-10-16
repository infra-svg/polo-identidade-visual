---
name: polo-identidade-visual
description: Cria peças da marca Pólo Soluções Elétricas (post, story, carrossel, folheto, documento, apresentação, assinatura, capa) seguindo o Guia Mestre da Identidade Visual. Também revisa peças prontas contra o guia. Use sempre que pedirem arte, mídia, material ou revisão de peça da Pólo.
---

# Pólo Soluções Elétricas — criação de peças

Fonte oficial das regras: Guia Mestre da Identidade Visual v1
- Nesta skill: references/guia-mestre-v1.md (leia a seção relevante em caso de dúvida)
- Doc vivo: https://claude.ai/code/artifact/fb4897a3-9066-4ece-908f-ab10da5a5ab9

Se houver conflito entre esta skill e o guia, o guia vence. Se o pedido conflitar com o guia, avise antes de produzir.

## 1. Dados fixos da marca

- Nome: Pólo Soluções Elétricas (nunca "Pólo Representações" em peças novas)
- Slogan: "Energia que transforma, soluções que conectam!"
- Trajetória: "Desde 1987" (nunca "há X anos")
- Atuação: materiais elétricos de média e alta tensão, Oeste Catarinense
- Telefones: (49) 3328-4315 (WhatsApp) · (49) 3304-3054
- E-mail: vendas@polorepres.com.br · Instagram: @polo.repres
- Endereço: Rua Ernesto Batista, 150-E · Chapecó-SC · 89809-320
- Representadas atuais: Itaipu Transformadores, Neo Cable, Vale, Incopostes

## 2. Fluxo de trabalho

1. Briefing. Confirme: formato, objetivo, título/mensagem, dados técnicos (potências, tensão, prazos, condições), foto disponível e CTA. O que faltar entra como [placeholder entre colchetes]. Nunca invente preço, estoque, prazo ou especificação.
2. Ativos. Logo: assets/logo/ desta skill (ou o SVG da seção 3). Fotos e logos de representadas: pasta do Drive "Mídias Pólo" (seção 9). Produto e pessoas sempre em foto real.
3. Montagem. Construa a peça em SVG/HTML no tamanho exato do formato (seção 7), usando só a paleta, as fontes e os grafismos desta skill.
4. Render. Gere PNG (digital) e também PDF (impressos A4). Ver seção 10.
5. Conferência. Rode o checklist da seção 11 olhando a imagem final (texto cortado, sobreposição, margens, linhas cruzando texto).
6. Entrega. Nome do arquivo: Polo_<Formato>_<Tema>.png/.pdf. Diga em uma linha o que é a peça e liste os placeholders e os dados que precisam ser conferidos.

## 3. Logo oficial (versão neon)

Arquivos-mestre (pasta assets/logo/ desta skill):
- assets/logo/polo-logo-neon-vetor.svg (textos em curvas, uso principal)
- assets/logo/polo-simbolo-neon-vetor.svg (sem descritor)
- assets/logo/polo-logo-neon-transparente.png (2000 px)
- assets/logo/polo-logo-neon-fundo-preto.png
- assets/logo/polo-simbolo-neon-transparente.png
- assets/logo/polo-logo-neon-editavel-fonte-poppins.svg (mesmo logo com texto editável; exige Poppins Bold)

Regras:
- Usar sempre sobre fundo escuro (Preto Pólo ou foto escurecida 70–85%).
- Em peça de fundo claro: o logo vai dentro de uma faixa ou bloco Preto Pólo (ex.: cabeçalho preto no documento A4). Nunca direto no branco.
- Usar só o arquivo-mestre. Nunca gerar logo por IA, redesenhar, recolorir, distorcer, inclinar ou colocar elementos sazonais sobre ele.
- Área de proteção: 10% da largura do logo em volta. Largura mínima: 160 px (com descritor) ou 110 px (símbolo).
- Posição: topo central em peças comerciais e de produto; rodapé central em peças institucionais e datas comemorativas; cabeçalho à esquerda em documentos.
- Usos sem brilho (bordado, carimbo, gravação, uma cor): setas #EE3016 chapadas + PÓLO #34086C (fundo claro) ou tudo em branco (fundo escuro), sem filtros.

SVG de referência (o mesmo de assets/logo/polo-logo-neon-editavel-fonte-poppins.svg; nome e descritor em Poppins Bold — carregue a fonte antes de renderizar ou use a versão em curvas):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
  <defs>
    <linearGradient id="redBody" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF5A33"/><stop offset="0.55" stop-color="#EE3016"/><stop offset="1" stop-color="#B8120A"/></linearGradient>
    <linearGradient id="redBody2" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FF5A33"/><stop offset="0.55" stop-color="#EE3016"/><stop offset="1" stop-color="#B8120A"/></linearGradient>
    <linearGradient id="blueFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5AD6FF"/><stop offset="0.5" stop-color="#14A9FA"/><stop offset="1" stop-color="#0A7BE8"/></linearGradient>
    <linearGradient id="silver" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.45" stop-color="#E4E8EE"/><stop offset="0.55" stop-color="#A9B1BD"/><stop offset="1" stop-color="#EEF1F5"/></linearGradient>
    <filter id="glowRed" x="-30%" y="-80%" width="160%" height="260%"><feGaussianBlur in="SourceAlpha" stdDeviation="16" result="b"/><feFlood flood-color="#FF2A10" flood-opacity="0.85"/><feComposite in2="b" operator="in"/></filter>
    <filter id="glowBlue" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur in="SourceAlpha" stdDeviation="14" result="b"/><feFlood flood-color="#1E7BFF" flood-opacity="0.9"/><feComposite in2="b" operator="in"/></filter>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="spark" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="4"/></filter>
    <filter id="shadow" x="-10%" y="-40%" width="120%" height="180%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.6"/></filter>
    <polygon id="arrowTop" points="120,325 618,120 546,212 880,325"/>
    <polygon id="arrowBot" points="880,640 382,845 454,753 120,640"/>
    <polygon id="arrowTopIn" points="190,307 566,152 500,226 820,307"/>
    <polygon id="arrowBotIn" points="810,658 434,813 500,739 180,658"/>
  </defs>
  <g id="setas">
    <g filter="url(#glowRed)"><use href="#arrowTop" fill="#000" stroke="#000" stroke-width="30" stroke-linejoin="round"/><use href="#arrowBot" fill="#000" stroke="#000" stroke-width="30" stroke-linejoin="round"/></g>
    <use href="#arrowTop" fill="url(#redBody)" stroke="#FF3A1E" stroke-width="30" stroke-linejoin="round"/>
    <use href="#arrowBot" fill="url(#redBody2)" stroke="#FF3A1E" stroke-width="30" stroke-linejoin="round"/>
    <use href="#arrowTop" fill="none" stroke="#FF8E6E" stroke-width="5" stroke-linejoin="round" opacity="0.85"/>
    <use href="#arrowBot" fill="none" stroke="#FF8E6E" stroke-width="5" stroke-linejoin="round" opacity="0.85"/>
    <use href="#arrowTopIn" fill="none" stroke="#FF9A80" stroke-width="3" stroke-linejoin="round" opacity="0.55"/>
    <use href="#arrowBotIn" fill="none" stroke="#FF9A80" stroke-width="3" stroke-linejoin="round" opacity="0.55"/>
    <g filter="url(#spark)" fill="#CFE6FF">
      <ellipse cx="560" cy="262" rx="60" ry="3" opacity="0.45" transform="rotate(-6 560 262)"/>
      <ellipse cx="430" cy="702" rx="60" ry="3" opacity="0.45" transform="rotate(-6 430 702)"/>
      <circle cx="520" cy="300" r="6" fill="#6FA8FF"/><circle cx="480" cy="665" r="6" fill="#6FA8FF"/>
    </g>
  </g>
  <g id="nome" font-family="Poppins" font-weight="700" font-size="236" letter-spacing="6" text-anchor="middle">
    <text x="500" y="586" filter="url(#glowBlue)" fill="#000" stroke="#000" stroke-width="24" stroke-linejoin="round">PÓLO</text>
    <text x="500" y="586" fill="#0B3FB5" stroke="#0B3FB5" stroke-width="24" stroke-linejoin="round">PÓLO</text>
    <text x="500" y="586" fill="url(#blueFill)" stroke="#E8FBFF" stroke-width="8" stroke-linejoin="round" paint-order="stroke">PÓLO</text>
    <text x="500" y="586" fill="none" stroke="#7FE0FF" stroke-width="3" stroke-linejoin="round" filter="url(#soft)" opacity="0.8">PÓLO</text>
  </g>
  <g id="descritor"><text x="500" y="948" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="66" letter-spacing="1" fill="url(#silver)" filter="url(#shadow)">SOLUÇÕES ELÉTRICAS</text></g>
</svg>
```

Ao inserir o logo dentro de outra peça SVG, envolva-o em `<g transform="translate(x,y) scale(s)">` e renomeie os ids (ex.: prefixo `lg-`) para não colidir com outros filtros da peça. Versão sem descritor: remover o grupo `descritor` e usar viewBox="0 70 1000 830".

## 4. Paleta

| Nome | HEX | Uso | Proporção |
| --- | --- | --- | --- |
| Vermelho Pólo | #EE3016 | CTA, fios, ícones de ação, 1 palavra do título | até 10% |
| Índigo Pólo | #34086C | Títulos e textos em fundo claro | 15% no claro |
| Ciano Elétrico | #06AFF9 | Destaques numéricos e linha de energia no escuro | até 5% |
| Preto Pólo | #0B0B0F | Fundo dominante do digital | 55–65% |
| Grafite | #1A1A20 | Cartões e molduras sobre o preto | 10–15% |
| Branco | #FFFFFF | Texto no escuro; fundo institucional | — |
| Azul Sinal | #0389F7 | Ícones dos pilares, ícones frios | até 5% |
| Névoa | #E8E7EA | Painéis claros, fundo de produto, tabelas | até 15% |
| Cinza Aço | #6B7384 | Texto secundário no claro | até 5% |
| Linha | #2E2E35 | Divisórias e contornos no escuro | até 3% |

No escuro, toda peça tem um destaque quente (Vermelho) e um frio (Ciano ou Azul Sinal). Nunca: Ciano como texto em fundo claro, fundo roxo, verde/amarelo (só sazonal declarado), carmim, gradientes violeta.

## 5. Tipografia

| Uso | Fonte | Tamanho no feed 1080 px |
| --- | --- | --- |
| Título de impacto | Barlow Condensed ExtraBold Itálico, caixa alta | 110–190 px, máx. 4 palavras por linha, 3 linhas |
| Título institucional | Montserrat ExtraBold, caixa alta | 72–96 px |
| Linha de apoio | Montserrat SemiBold, caixa alta, entreletra +200 | 26–32 px, ladeada por fios vermelhos curtos |
| Texto | Montserrat Regular/Medium | 28–32 px (mín. 24) |
| Números e potências | Barlow Condensed Bold Itálico + unidade em Montserrat SemiBold a 50% | 56–80 px |
| Tabelas/técnico | Montserrat Medium; cabeçalho SemiBold caixa alta | 22–26 px |
| Destaque emocional | Kaushan Script | 1 vez por peça, até 4 palavras, só datas/marcos |

Carregar via Google Fonts (`family=Montserrat:wght@400;500;600;700;800&family=Barlow+Condensed:ital,wght@1,700;1,800&family=Kaushan+Script&family=Poppins:wght@700`) e esperar `document.fonts.ready` antes de capturar. Sem acesso: Poppins no lugar de Montserrat e avisar na entrega. Máximo 3 níveis de hierarquia por peça.

## 6. Grafismos

- Raio-marcador (listas técnicas, tarjas): `<path d="M13 2 L4 14 H11 L10 22 L20 9 H13 Z" fill="#EE3016"/>` em grade 24×24, escalado à altura da maiúscula.
- Linhas de energia (só fundo preto, 2 cantos opostos, nunca cruzando texto ou molduras): vermelha no canto superior esquerdo `M0 460 L190 270 L500 270`, ciano no inferior direito espelhada; traço 6 px com brilho (feGaussianBlur 9 + flood da cor).
- Moldura chanfrada (1 por peça): retângulo com cantos cortados a 45°, chanfro = 4% da largura, contorno 4–5 px Vermelho Pólo, interior Grafite (ou Névoa quando contém foto de produto com fundo claro).
- Tarja-rótulo: pílula Preto Pólo, raio-marcador vermelho e texto Barlow branco em caixa alta. Máx. 3.
- Fio divisório: 2–3 px Vermelho Pólo no claro; Linha #2E2E35 no escuro.
- Trio de pilares (fechamento institucional): ícone de linha 2 px em círculo Azul Sinal + rótulo. Rótulos fixos: CONFIANÇA, PARCERIAS, SOLUÇÕES (+ QUALIDADE na assinatura).
- Faixa de representadas: sempre no rodapé, logos com altura ≤ 60% do logo Pólo, separados por fios verticais, título "REPRESENTADAS" (Montserrat SemiBold +200).
- Selo "DESDE 1987": Montserrat Medium +200 entre dois fios curtos brancos, abaixo do logo.
- Ícones: um único estilo de linha 2 px, cantos arredondados. Sem emojis.

## 7. Formatos e estrutura

Estrutura em três faixas: topo (marca + título, 15–20%), centro (produto/foto/informação, 55–65%), base (representadas, pilares ou CTA + contato, 15–20%). Margem lateral 6% (64 px no 1080). Espaçamentos em múltiplos de 8. Espaço negativo mínimo 25%. Máx. 40 palavras no feed, 25 no story, 5 itens por lista. Pólo sempre maior que qualquer representada.

| Formato | Tamanho | Fundo | Estrutura |
| --- | --- | --- | --- |
| Post produto/oferta | 1080×1350 | Preto + linhas de energia | Logo topo → apoio + título → moldura com produto e potências → CTA em pílula → representadas |
| Post institucional/data | 1080×1350 | Foto real escurecida | Apoio (data) → título → 1 frase script → foto → faixa preta com logo + trio de pilares |
| Post estoque/tabela | 1080×1350 | Faixa superior preta + Névoa | Título na faixa → tarjas Monofásicos/Trifásicos → potências "112,5 kVA \| 25 kV" + foto → rodapé com contato |
| Carrossel | 1080×1350, 3–8 lâminas | Preto | Capa com logo; 1 ideia por lâmina; numeração "01/06" em Barlow no canto superior direito; última = CTA + contato + representadas |
| Story | 1080×1920 | Preto | Zonas livres de 250 px no topo e na base. Logo a partir de y≈260 → apoio → título → moldura → CTA (WhatsApp) acima de y 1670 |
| Capa de rede social | conforme a rede | Paisagem de energia golden hour escurecida | Logo no terço central, slogan abaixo, nada sob a foto de perfil |
| Avatar | 1080×1080 | Preto | Símbolo (sem descritor) a 70% da largura |
| Folheto A4 | 1240×1754 (150 dpi) | Preto com radial suave + rodapé branco | Logo + Desde 1987 → título (slogan) → subtítulo → moldura de produtos → cartões de linhas → CTA vermelho cheio → rodapé com representadas e contatos |
| Documento A4 (proposta, comunicado) | 1240×1754 (150 dpi) | Branco com cabeçalho preto (≈200 px) | Logo no cabeçalho à esquerda + nº/data à direita → fio vermelho → título Montserrat ExtraBold Índigo → bloco Névoa de dados → texto → tabela (cabeçalho Índigo, linhas alternadas Névoa) → condições com raio-marcador → assinatura → rodapé com representadas, contatos e barra vermelho/índigo |
| Apresentação | 16:9 | Capa/divisórias preto; miolo branco com logo só em faixa preta | Título Montserrat ExtraBold Índigo à esquerda, fio vermelho, número da página |
| Assinatura de e-mail | 800×150 | Bloco preto à esquerda com logo; restante branco | Nome Montserrat Bold Índigo, cargo, contatos com ícones, representadas, fio vermelho |

Exemplos aprovados em teste: assets/exemplos/ (story, folheto e documento padrão). Pranchas do guia: assets/pranchas/. Revisar uma peça pronta: references/revisao-12-criterios.md. IDs completos do Drive: references/ativos-google-drive.md.

## 8. Imagens

- Produto: foto real, inteira, 3/4 ou frente, 45–60% da altura. Sobre preto (recorte com luz vermelha/azul) ou dentro de painel Névoa/branco do tamanho da foto.
- Pessoas: equipe real, uniforme marinho com logo visível, olhar para a câmera. Nunca banco de imagens genérico (aperto de mão, escritório).
- Paisagem de energia (capas e institucional): golden hour, horizonte no terço inferior.
- IA: só para fundos conceituais, sempre escurecidos 70–85%, sem textos ou logos inventados. Nunca produto, pessoa ou logo por IA.

## 9. Ativos no Google Drive (pasta "Mídias Pólo", id 1Rjlt1Cjk4q2mfhkvQjK7XCeqth9VFSY1)

Miniatura utilizável: https://drive.google.com/thumbnail?id=<ID>&sz=w1600

- Transformador trifásico Itaipu (fundo claro, 4:5): 1TTLvzFrsQlQgueavQZu-MRzGWNEGVGUb
- Transformador monofásico Itaipu (fundo branco, 2:3): 18sW8UEcAdbg8HZZzp23E7noufllkqo4g
- Logo Itaipu (recortar a borda preta com cantos arredondados): 1nn5bHejnPZe9lZBUxHTl0uL56OGVAYmY
- Logo Neo Cable: 1y3GM8z0dA8ddjvlURC3KhSq9laQM9qZX
- Logo Vale: 1VOvVVlYTmkQq0DlEEnLO72-xaXm3LULd
- Logo Incopostes: não há arquivo isolado na pasta; peça à usuária ou omita e avise.
- Fotos de equipe e eventos: subpasta "5ª Convenção" e arquivos SAVE_20260531_*.

## 10. Render

- Monte a peça como SVG/HTML no tamanho final, com as fontes carregadas.
- Capture com navegador (Playwright ou Claude in Chrome). Script desta skill: `python <pasta-da-skill>/scripts/render_svg.py <arquivo.svg> <saida.png> <largura> <altura> [cor_de_fundo|transparent]`.
- Exporte PNG para digital; PNG + PDF para A4.
- Antes de entregar, olhe a imagem final inteira e em zoom nas áreas de texto e logo.

## 11. Checklist final (tudo precisa passar)

1. Logo do arquivo-mestre, sobre fundo escuro, sem distorção, com área de proteção.
2. Logo Pólo presente e maior que as representadas.
3. Só cores da paleta; no escuro, um destaque quente e um frio.
4. Só as três famílias tipográficas, nos usos da tabela; máx. 3 níveis.
5. Estrutura de três faixas; margem 64 px; zonas livres no story.
6. Nenhum texto cortado, sobreposto ou cruzado por linha/grafismo.
7. Foto real para produto e pessoas.
8. Nome "Pólo Soluções Elétricas", "Desde 1987", contatos corretos.
9. Potências no padrão "112,5 kVA | 25 kV".
10. Nenhum dado inventado; pendências em [colchetes] listadas na entrega.
