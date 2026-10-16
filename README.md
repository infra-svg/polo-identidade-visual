# Pólo Soluções Elétricas — Skill de identidade visual

Skill para o Claude Code que cria e revisa peças da marca Pólo Soluções Elétricas (post, story, carrossel, folheto, documento A4, apresentação, assinatura de e-mail, capa) seguindo o Guia Mestre da Identidade Visual v1.

## Conteúdo

```
polo-identidade-visual/
├── SKILL.md                 regras de produção da marca
├── references/              guia mestre, revisão em 12 critérios, IDs do Google Drive
├── assets/logo/             logo oficial neon (SVG e PNG)
├── assets/pranchas/         pranchas do guia
├── assets/exemplos/         peças aprovadas (story, folheto, documento A4)
└── scripts/render_svg.py    render SVG → PNG
```

## Instalação

Copie a pasta `polo-identidade-visual` para a pasta de skills do Claude Code:

- Windows: `%USERPROFILE%\.claude\skills\`
- macOS/Linux: `~/.claude/skills/`

```bash
git clone https://github.com/infra-svg/polo-identidade-visual.git
cp -r polo-identidade-visual/polo-identidade-visual ~/.claude/skills/
```

Para gerar PNG/PDF (opcional):

```bash
pip install playwright
python -m playwright install chromium
```

Reinicie o Claude Code depois de instalar.

## Exemplos de pedidos

- "Cria um post de produto do transformador trifásico Itaipu"
- "Faz um story de pronta entrega"
- "Monta um documento A4 de proposta comercial"
- "Revisa esta arte da Pólo" (anexando a imagem)

Guia vivo: https://claude.ai/code/artifact/fb4897a3-9066-4ece-908f-ab10da5a5ab9
