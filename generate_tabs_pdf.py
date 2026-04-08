from playwright.sync_api import sync_playwright
import os

def generate_pdf():
    html_path = "file://" + os.path.abspath("index.html")
    pdf_outputs = []

    with sync_playwright() as p:
        print("Lancement du navigateur Chrome en arrière-plan...")
        browser = p.chromium.launch()
        # On définit une grande fenêtre pour forcer l'affichage bureautique
        page = browser.new_page(viewport={"width": 1440, "height": 1080})
        
        print("Chargement de la page Atout Soleil...")
        page.goto(html_path)
        page.wait_for_selector(".bg-white", timeout=30000)
        page.wait_for_timeout(1000)
        
        # Les boutons des 4 onglets dans le header
        tabs = page.query_selector_all("header button")
        
        for i, tab in enumerate(tabs):
            tab.click()
            print(f"Capture de l'onglet {i+1}/4...")
            # On attend que l'animation "fade-in" soit complètement finie
            page.wait_for_timeout(1500)
            
            # On calcule la hauteur totale requise pour cet onglet pour ne pas le couper
            height = page.evaluate("document.documentElement.scrollHeight")
            width = page.evaluate("document.documentElement.scrollWidth")
            
            # On rajoute une toute petite marge en bas
            height = height + 40
            
            out_name = f"temp_tab_{i}.pdf"
            pdf_outputs.append(out_name)
            
            # On génère une page PDF sur mesure pour cet onglet
            page.pdf(
                path=out_name,
                width=f"{width}px",
                height=f"{height}px",
                print_background=True,
                page_ranges="1" # Une seule grande page continue
            )
            
        browser.close()
        print("Fusion des onglets en un seul fichier PDF...")
        
    # On rassemble tous les PDF temporaires en un seul fichier avec pypdf
    try:
        from pypdf import PdfWriter
        merger = PdfWriter()
        for pdf in pdf_outputs:
            merger.append(pdf)
            
        final_pdf = os.path.abspath("Comparateur_Atout_Soleil_2026.pdf")
        merger.write(final_pdf)
        merger.close()
        
        # Nettoyage des petits morceaux
        for pdf in pdf_outputs:
            if os.path.exists(pdf):
                os.remove(pdf)
                
        print(f"Succès ! Le fichier est prêt : {final_pdf}")
    except Exception as e:
        print(f"Erreur lors de la fusion : {e}")

if __name__ == "__main__":
    generate_pdf()
