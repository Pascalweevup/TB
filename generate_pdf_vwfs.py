import os
import re
import sys
import subprocess
import time

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Installing playwright...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "PyPDF2"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright

from PyPDF2 import PdfMerger

def create_print_html(source_path, dest_path, force_tab):
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if force_tab == 'summary':
        tab_component = '<ComparisonView />'
        view_type = 'Synthèse'
    else:
        tab_component = '<VenueDetailView venueId="tournee" />'
        view_type = 'Détaillée'

    app_replacement = f"""
        function App() {{
            return (
                <div className="bg-slate-50 font-sans" style={{{{padding: '40px'}}}}>
                    <header className="bg-white shadow-sm border border-gray-200 mb-8 p-6 rounded-xl">
                        <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-2">
                            VOLKSWAGEN FINANCIAL SERVICES — Séminaire 2026
                        </h1>
                        <p className="text-sm text-gray-500 mt-2">Vue {view_type} des Tournées Régionales</p>
                    </header>
                    <main className="max-w-7xl mx-auto">
                        {tab_component}
                    </main>
                </div>
            );
        }}
    """
    
    content = re.sub(r'function App\(\)\s*\{.*?\}\s*(?=// Mount the app)', app_replacement, content, flags=re.DOTALL)

    style_print = """
        <style>
            body { background-color: #f8fafc !important; }
            .shadow-sm { box-shadow: none !important; border: 1px solid #e2e8f0 !important; }
            * { animation: none !important; transition: none !important; opacity: 1 !important; transform: none !important; }
        </style>
    """
    content = content.replace("</style>", "</style>\n" + style_print)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

def run():
    source = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
    summary_html = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/print_summary.html"
    detail_html = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/print_detail.html"
    
    create_print_html(source, summary_html, 'summary')
    create_print_html(source, detail_html, 'detail')
    
    output_pdf = "/Users/lolaricharte/Desktop/Budget_VWFS_2026.pdf"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.on("console", lambda msg: print(f"Browser log: {msg.text}"))
        
        # summary
        url_summary = "file://" + summary_html
        print(f"Loading {url_summary}...")
        page.goto(url_summary)
        page.wait_for_selector('main > div', timeout=20000)
        time.sleep(2)
        height1 = page.evaluate("document.documentElement.scrollHeight + 40")
        page.pdf(path="summary.pdf", print_background=True, width="1400px", height=f"{height1}px", page_ranges="1")

        # detail
        url_detail = "file://" + detail_html
        print(f"Loading {url_detail}...")
        page.goto(url_detail)
        page.wait_for_selector('main > div', timeout=20000)
        time.sleep(2)
        height2 = page.evaluate("document.documentElement.scrollHeight + 40")
        page.pdf(path="detail.pdf", print_background=True, width="1400px", height=f"{height2}px", page_ranges="1")
        
        browser.close()

    merger = PdfMerger()
    merger.append("summary.pdf")
    merger.append("detail.pdf")
    merger.write(output_pdf)
    merger.close()
    
    os.remove("summary.pdf")
    os.remove("detail.pdf")
    os.remove(summary_html)
    os.remove(detail_html)
    
    print(f"PDF successfully generated at {output_pdf}")

if __name__ == "__main__":
    run()
