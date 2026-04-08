from playwright.sync_api import sync_playwright
import os

def generate_pdf():
    html_path = "file://" + os.path.abspath("print.html")
    pdf_path = os.path.abspath("Comparateur_Atout_Soleil_2026.pdf")

    with sync_playwright() as p:
        print("Lancement du navigateur en arrière-plan...")
        browser = p.chromium.launch()
        page = browser.new_page()
        
        print("Ouverture de la page et attente du chargement de React...")
        page.goto(html_path)
        
        # On attend spécifiquement que la classe .bg-white apparaisse
        # Cela nous garantit que React et Babel ont fini de charger
        page.wait_for_selector(".bg-white", timeout=30000)
        
        # On attend une petite seconde supplémentaire pour les animations CSS
        page.wait_for_timeout(2000)
        
        print("Génération du PDF...")
        page.pdf(
            path=pdf_path, 
            format="A4", 
            print_background=True,
            margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"}
        )
        
        browser.close()
        print(f"PDF généré avec succès : {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
