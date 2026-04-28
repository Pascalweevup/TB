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
                    <div style={{ pageBreakAfter: 'always', paddingBottom: '40px', minHeight: '100vh' }}>
                        <header className="bg-white shadow-sm border-b border-gray-200 mb-8 p-4">
                            <h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                                KPMG — Séminaire Financier
                            </h1>
                            <p className="text-sm text-gray-500">Comparateur interactif de propositions événementielles</p>
                        </header>
                        <main className="max-w-7xl mx-auto px-4">
                            <ComparisonView />
                        </main>
                    </div>

                    {Object.values(budgetData).map(venue => (
                        <div key={venue.id} style={{ pageBreakAfter: 'always', paddingBottom: '40px', minHeight: '100vh' }}>
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

    # Styles d'impression optimisés pour éviter les coupures
    style_print = """
        @media print {
            body { 
                -webkit-print-color-adjust: exact; 
                print-color-adjust: exact; 
                background-color: #f8fafc !important;
                width: 100%;
            }
            .shadow-sm { box-shadow: none !important; border: 1px solid #e2e8f0 !important; }
            /* Désactiver les animations */
            * { 
                animation: none !important; 
                transition: none !important; 
                opacity: 1 !important; 
                transform: none !important; 
            }
            @page {
                size: A4 portrait;
                margin: 10mm;
            }
            /* Éviter les coupures à l'intérieur des blocs importants */
            .bg-white.rounded-xl, .bg-white.rounded-lg {
                break-inside: avoid;
                page-break-inside: avoid;
            }
        }
    """
    content = content.replace("</style>", style_print + "\n    </style>")

    with open('print.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Fichier print.html généré.")
    
    pdf_path = "/Users/lolaricharte/Desktop/Budget_KPMG_Final.pdf"
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
    
    print("Génération du PDF en cours...")
    subprocess.run(cmd, check=True)
    print(f"PDF généré avec succès : {pdf_path}")

if __name__ == "__main__":
    generate()
