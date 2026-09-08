from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FILES = ["flyer-parrilla-1x1-opcionA.html", "flyer-parrilla-1x1-opcionB.html", "flyer-parrilla-1x1-opcionC.html"]
OUT_DIR = ROOT / "output" / "revision-parrilla"
OUT_DIR.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.set_default_timeout(60000)
    for name in FILES:
        url = (ROOT / "plantillas" / name).as_uri()
        page.goto(url, wait_until="load", timeout=60000)
        page.wait_for_timeout(500)
        out_path = OUT_DIR / (name.replace(".html", ".png"))
        page.screenshot(path=str(out_path), timeout=60000)
        print("saved", out_path)
    browser.close()
