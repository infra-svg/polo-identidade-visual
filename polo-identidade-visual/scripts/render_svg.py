"""Renderiza um arquivo SVG em PNG usando Chromium (Playwright), com fontes do Google Fonts.

Uso:
    python scripts/render_svg.py entrada.svg saida.png LARGURA ALTURA [fundo]

    fundo: cor CSS (ex.: "#0B0B0F") ou "transparent" (padrao).

Requisitos:
    pip install playwright
    python -m playwright install chromium
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

FONTES = (
    "https://fonts.googleapis.com/css2?"
    "family=Montserrat:wght@400;500;600;700;800"
    "&family=Barlow+Condensed:ital,wght@1,700;1,800"
    "&family=Kaushan+Script&family=Poppins:wght@700&display=block"
)


def main() -> None:
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)
    entrada, saida = Path(sys.argv[1]), Path(sys.argv[2])
    largura, altura = int(sys.argv[3]), int(sys.argv[4])
    fundo = sys.argv[5] if len(sys.argv) > 5 else "transparent"

    svg = entrada.read_text(encoding="utf-8")
    html = (
        f"<html><head><link rel='stylesheet' href='{FONTES}'>"
        f"<style>html,body{{margin:0;background:{fundo}}}"
        f"svg{{width:{largura}px;height:{altura}px;display:block}}</style></head>"
        f"<body>{svg}</body></html>"
    )
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page(viewport={"width": largura, "height": altura})
        pagina.set_content(html, wait_until="networkidle")
        pagina.evaluate("document.fonts.ready")
        pagina.wait_for_timeout(300)
        pagina.screenshot(path=str(saida), omit_background=(fundo == "transparent"))
        navegador.close()
    print(f"OK: {saida}")


if __name__ == "__main__":
    main()
