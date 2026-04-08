import re
import os
import subprocess
import time

# Options pour Chrome headless
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def generate():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacement du composant App pour afficher toutes les vues
    app_replacement = """
        function App() {
            return (
                <div className="bg-slate-50 font-sans">
                    <div style={{ pageBreakAfter: 'always', paddingBottom: '20px' }}>
                        <header className="bg-white shadow-sm border-b border-gray-200 mb-8 p-4">
                            <h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                                <span className="text-yellow-500">☀️</span> Fromont Briens — Séminaire 2026
                            </h1>
                            <p className="text-sm text-gray-500">Comparateur interactif de propositions événementielles</p>
                        </header>
                        <main className="max-w-7xl mx-auto px-4">
                            <ComparisonView />
                        </main>
                    </div>

                    {Object.values(budgetData).map(venue => (
                        <div key={venue.id} style={{ pageBreakAfter: 'always', paddingBottom: '20px' }}>
                            <main className="max-w-7xl mx-auto px-4">
                                <VenueDetailView venueId={venue.id} />
                            </main>
                        </div>
                    ))}
                </div>
            );
        }
    """
    
    # Remplacer la fonction App
    content = re.sub(r'function App\(\)\s*\{.*?\}\s*(?=// Mount the app)', app_replacement, content, flags=re.DOTALL)

    # Ajouter quelques styles d'impression pour forcer l'affichage sans délai et sur 1 page/onglet
    style_print = """
        @media print {
            body { -webkit-print-color-adjust: exact; print-color-adjust: exact; background-color: #f8fafc !important; }
            .shadow-sm { box-shadow: none !important; border: 1px solid #e2e8f0 !important; }
            /* Désactiver les animations pour que le contenu ne soit pas invisible dans Chrome Headless (opacity 0) */
            * { animation: none !important; transition: none !important; opacity: 1 !important; transform: none !important; }
            @page {
                size: A3 landscape;
                margin: 0;
            }
        }
    """
    content = content.replace("</style>", style_print + "\n    </style>")

    with open('print.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Fichier print.html généré.")
    
    # On ajoute un délai directement dans l'html pour signifier à puppet/chrome que c'est prêt
    # mais Chrome avec --virtual-time-budget fait déjà le job.
    
    pdf_path = "/Users/lolaricharte/Desktop/Budget_Fromont_V2.pdf"
    html_url = "file://" + os.path.join(os.getcwd(), "print.html")
    
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=" + pdf_path,
        "--no-pdf-header-footer",
        "--virtual-time-budget=5000",
        html_url
    ]
    
    print("Génération du PDF en cours via Chrome...")
    subprocess.run(cmd, check=True)
    print(f"PDF généré avec succès à l'emplacement : {pdf_path}")

if __name__ == "__main__":
    generate()
