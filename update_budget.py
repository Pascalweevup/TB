import os

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volks-budget — Tournées Régionales 2026</title>
    <meta name="description" content="Budget détaillé Tournées Régionales 2026">
    <script src="https://cdn.tailwindcss.com"></script>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.4s ease-out; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState } = React;

        const budgetData = {
            id: 'tournee_regionale',
            name: "Tournées Régionales 2026",
            totalTTC: 131785.92, // 109821.60 * 1.2
            totalHT: 109821.60,
            honorairesHT: 17250.00, // Considered partially as honoraires (Personnel & Conception)
            categories: {
                personnel: 17250.00,
                technique: 7562.10,
                lieux: 61875.80,
                logistique: 18475.48,
                frais_annexes: 4658.22
            },
            details: {
                personnel: [
                    { desc: "Pilotage de projet", price: 6150.00, subDesc: "Directeur de clientèle (2x 900€) = 1800€\\nDirecteur des projets (5x 600€) = 3000€\\nChef de projet (3x 450€) = 1350€" },
                    { desc: "Equipe logistique", price: 11100.00, subDesc: "Directeur logistique amont (2x 600€) = 1200€\\nAssistant logistique amont (2x 450€) = 900€\\nDirecteur logistique sur sites (12x 600€) = 7200€\\nRégisseur général terrain (4x 450€) = 1800€" }
                ],
                technique: [
                    { desc: "Audio, Vidéo, Lumière & Mobilier - Village Blanc 5*", price: 1950.00, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\\nVidéo, Lumière, Mobilier inclus" },
                    { desc: "Audio, Vidéo, Lumière & Mobilier - La Villa La Coste", price: 2167.10, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\\nVidéo, Lumière, Mobilier inclus" },
                    { desc: "Audio, Vidéo, Lumière & Mobilier - Zoo de Beauval", price: 1950.00, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\\nVidéo, Lumière, Mobilier inclus" },
                    { desc: "Audio, Vidéo, Lumière & Mobilier - G.H. Mumm", price: 1495.00, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\\nVidéo, Lumière, Mobilier inclus" }
                ],
                lieux: [
                    { desc: "Lyon : Village Blanc 5*", price: 10659.34, subDesc: "Location salle : 1625€\\nAccueil & Restauration : Cocktails et Dîners (50 et 7 pax) : 6326.69€\\nHébergement (7 pax) : 2705.15€ + Taxes" },
                    { desc: "Aix en Provence / Avignon : La Villa La Coste", price: 18456.61, subDesc: "Location salle : 5417.10€\\nSéminaire & Restauration : Cocktails et Dîner (50 et 7 pax) : 9272.60€\\nHébergement (7 pax) : 3749.20€ + Taxes" },
                    { desc: "Le Mans : Zoo de Beauval", price: 11745.44, subDesc: "Location salle & Accès zoo : 4208.73€\\nRestauration : Déjeuners et Dîner (80 et 7 pax) : 5384.28€\\nAgent de sécurité : 216.67\\nHébergement (7 pax) : 1613.29€ + Taxes" },
                    { desc: "Reims : G.H. Mumm", price: 21014.41, subDesc: "Location salle & Privatisation : 3333.20€\\nRestauration : Accueil & Cocktail (80 pax), Dîner (7 pax) : 15999.11€\\nHébergement (7 pax) : 1662.85€ + Taxes" }
                ],
                logistique: [
                    { desc: "Plateforme de gestion et inscriptions", price: 8520.40, subDesc: "Plateforme, e-mailing, SMS, Enquête satisfaction & Badges" },
                    { desc: "Signalétique", price: 2160.00, subDesc: "4 rolls up et 4 oriflammes, avec création graphique" },
                    { desc: "Acheminement et transferts", price: 8987.44, subDesc: "Transports en train (1987.44€) et véhicules avec chauffeur (Crafter) zones Sud et Nord (7000.00€)" },
                    { desc: "Accueil sites", price: 610.14, subDesc: "Hôtesses d'accueil sur les différents sites" },
                    { desc: "Gestion des véhicules", price: 357.50, subDesc: "Péages et carburant" }
                ],
                frais_annexes: [
                    { desc: "Hébergement Staff (VHR)", price: 2080.00, subDesc: "4 nuitées pour 2 Weevers" },
                    { desc: "Restauration Staff (VHR)", price: 936.00, subDesc: "2 repas pour 4 Weevers (24 pax au total)" },
                    { desc: "Déplacements Staff (VHR)", price: 1642.22, subDesc: "Taxi, véhicules de location et trains" }
                ]
            }
        };

        const categoryLabels = {
            personnel: "Personnel & Conception",
            technique: "Frais Techniques",
            lieux: "Lieux et Frais Relatifs",
            logistique: "Logistique Événementielle",
            frais_annexes: "Frais de Vie & Annexes"
        };

        const categoryColors = {
            personnel: "bg-blue-500",
            technique: "bg-purple-500",
            lieux: "bg-orange-500",
            logistique: "bg-slate-500",
            frais_annexes: "bg-teal-500"
        };

        const formatEur = (value) => new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(value);

        const IconChart = () => <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><path d="M3 9h18"></path><path d="M9 21V9"></path></svg>;
        const IconList = () => <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>;

        const SummaryView = () => {
            return (
                <div className="space-y-8 animate-fade-in">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 flex flex-col justify-center items-center text-center">
                            <h3 className="text-xl font-medium text-gray-500 mb-2">Budget Total Estimatif (HT)</h3>
                            <p className="text-5xl font-extrabold text-sky-900 mb-4">{formatEur(budgetData.totalHT)}</p>
                            <p className="text-sm text-gray-400">Total TTC estimé : {formatEur(budgetData.totalTTC)}</p>
                        </div>
                        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 flex flex-col justify-center">
                            <h3 className="text-lg font-semibold text-gray-900 mb-4">Répartition par pôle</h3>
                            <div className="space-y-4">
                                {Object.entries(budgetData.categories).map(([catKey, catValue]) => {
                                    const percentage = (catValue / budgetData.totalHT) * 100;
                                    return (
                                        <div key={catKey}>
                                            <div className="flex justify-between text-sm font-medium mb-1">
                                                <span className="text-gray-700 flex items-center gap-2">
                                                    <span className={`w-2 h-2 rounded-full ${categoryColors[catKey]}`}></span>
                                                    {categoryLabels[catKey]}
                                                </span>
                                                <span className="text-gray-900">{formatEur(catValue)} ({percentage.toFixed(1)}%)</span>
                                            </div>
                                            <div className="w-full bg-gray-100 rounded-full h-2">
                                                <div className={`h-2 rounded-full ${categoryColors[catKey]}`} style={{ width: `${percentage}%` }}></div>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                </div>
            );
        };

        const DetailView = () => {
            return (
                <div className="space-y-6 animate-fade-in">
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                        <h2 className="text-2xl font-bold text-gray-900 mb-6">Détail des prestations</h2>
                        <div className="space-y-8">
                            {Object.entries(budgetData.categories).map(([catKey, catValue]) => {
                                const percentage = ((catValue / budgetData.totalHT) * 100).toFixed(1);
                                return (
                                    <div key={catKey} className="bg-gray-50 rounded-xl border border-gray-200 overflow-hidden">
                                        <div className={`p-4 flex items-center justify-between border-b border-gray-200 bg-white`}>
                                            <div className="flex items-center gap-3">
                                                <div className={`w-3 h-8 rounded-full ${categoryColors[catKey]}`}></div>
                                                <h3 className="text-lg font-bold text-gray-900">{categoryLabels[catKey]}</h3>
                                            </div>
                                            <div className="text-right">
                                                <p className="text-xl font-bold text-gray-900">{formatEur(catValue)}</p>
                                                <p className="text-xs text-gray-500 font-medium tracking-wide">SOUS-TOTAL HT</p>
                                            </div>
                                        </div>
                                        <div className="p-0">
                                            {budgetData.details[catKey].map((item, idx) => (
                                                <div key={idx} className="flex flex-col sm:flex-row sm:items-center justify-between p-4 border-b border-gray-200 last:border-0 bg-white/50 hover:bg-white transition-colors">
                                                    <div className="mb-2 sm:mb-0 max-w-2xl">
                                                        <p className="font-semibold text-gray-800">{item.desc}</p>
                                                        {item.subDesc && (
                                                            <p className="text-sm text-gray-500 mt-1 leading-relaxed whitespace-pre-line">{item.subDesc}</p>
                                                        )}
                                                    </div>
                                                    <div className="font-bold text-gray-900 sm:text-right whitespace-nowrap">
                                                        {formatEur(item.price)}
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </div>
            );
        };

        function App() {
            const [activeTab, setActiveTab] = useState('summary');

            return (
                <div className="min-h-screen bg-slate-50 pb-12 font-sans">
                    <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
                        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
                            <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
                                <div>
                                    <h1 className="text-2xl font-bold text-gray-900 flex items-center gap-3">
                                        <span className="text-blue-600 bg-blue-100 p-2 rounded-lg"><IconChart /></span> 
                                        {budgetData.name}
                                    </h1>
                                    <p className="text-sm text-gray-500 mt-1">Détails de l'offre financière — Volkswagen Bank</p>
                                </div>

                                <div className="flex space-x-2 bg-gray-100 p-1.5 rounded-xl">
                                    <button
                                        onClick={() => setActiveTab('summary')}
                                        className={`flex items-center gap-2 px-5 py-2.5 text-sm font-semibold rounded-lg transition-all ${activeTab === 'summary' ? 'bg-white text-sky-700 shadow-sm ring-1 ring-gray-200/50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-200/50'}`}
                                    >
                                        <IconChart /> Vue Synthèse
                                    </button>
                                    <button
                                        onClick={() => setActiveTab('detail')}
                                        className={`flex items-center gap-2 px-5 py-2.5 text-sm font-semibold rounded-lg transition-all ${activeTab === 'detail' ? 'bg-white text-sky-700 shadow-sm ring-1 ring-gray-200/50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-200/50'}`}
                                    >
                                        <IconList /> Vue Détaillée
                                    </button>
                                </div>
                            </div>
                        </div>
                    </header>

                    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8">
                        {activeTab === 'summary' ? <SummaryView /> : <DetailView />}
                    </main>
                </div>
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "w", encoding="utf-8") as f:
    f.write(html_content)
