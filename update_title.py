import os

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace title
html = html.replace("<title>Volkswagen Bank — Tournées Régionales 2026</title>", "<title>VOLKSWAGEN FINANCIAL SERVICES — Tournées Régionales 2026</title>")

# Replace H1
old_h1 = """<h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                                        <span className="text-yellow-500">☀️</span> Volkswagen Bank — Séminaire 2026
                                    </h1>"""
new_h1 = """<h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                                        VOLKSWAGEN FINANCIAL SERVICES — Séminaire 2026
                                    </h1>"""
html = html.replace(old_h1, new_h1)

# Ensure no other "Volkswagen Bank" remain
html = html.replace("Volkswagen Bank", "VOLKSWAGEN FINANCIAL SERVICES")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
