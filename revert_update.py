import os

html_content = r"""<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volkswagen Bank — Tournées Régionales 2026</title>
    <meta name="description" content="Budget interactif des Tournées Régionales 2026">

    <!-- Tailwind CSS via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- React & ReactDOM via CDN -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

    <!-- Babel Standalone for JSX in-browser transpilation -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(8px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .animate-fade-in {
            animation: fadeIn 0.4s ease-out;
        }

        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }

        ::-webkit-scrollbar-track {
            background: transparent;
        }

        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 3px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
    </style>
</head>

<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState } = React;

        // --- DATA EXTRACTED FROM PDFs V2 ---
        const budgetData = {
            tournee: {
                id: 'tournee',
                name: "Tournées Régionales 2026",
                totalTTC: 131785.92,
                totalHT: 109821.60,
                honorairesHT: 17250.00,
                categories: {
                    personnel: 17250.00,
                    technique: 7562.10,
                    lieux: 61875.80,
                    logistique: 18475.48,
                    frais_annexes: 4658.22
                },
                details: {
                    personnel: [
                        { desc: "Pilotage de projet", price: 6150.00, subDesc: "Directeur de clientèle (2x 900€) = 1800€\nDirecteur des projets (5x 600€) = 3000€\nChef de projet (3x 450€) = 1350€" },
                        { desc: "Equipe logistique", price: 11100.00, subDesc: "Directeur logistique amont (2x 600€) = 1200€\nAssistant logistique amont (2x 450€) = 900€\nDirecteur logistique sur sites (12x 600€) = 7200€\nRégisseur général terrain (4x 450€) = 1800€" }
                    ],
                    technique: [
                        { desc: "Audio, Vidéo, Lumière & Mobilier - Village Blanc 5*", price: 1950.00, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\nVidéo, Lumière, Mobilier inclus" },
                        { desc: "Audio, Vidéo, Lumière & Mobilier - La Villa La Coste", price: 2167.10, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\nVidéo, Lumière, Mobilier inclus" },
                        { desc: "Audio, Vidéo, Lumière & Mobilier - Zoo de Beauval", price: 1950.00, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\nVidéo, Lumière, Mobilier inclus" },
                        { desc: "Audio, Vidéo, Lumière & Mobilier - G.H. Mumm", price: 1495.00, subDesc: "Forfait sonorisation incluant 5 micros cravate, logistique et personnel\nVidéo, Lumière, Mobilier inclus" }
                    ],
                    lieux: [
                        { desc: "Lyon : Village Blanc 5*", price: 10659.34, subDesc: "Location salle : 1625€\nAccueil & Restauration (50 et 7 pax) : 6326.69€\nHébergement (7 pax) : 2705.15€" },
                        { desc: "Aix en Provence / Avignon : La Villa La Coste", price: 18456.61, subDesc: "Location salle : 5417.10€\nSéminaire & Restauration (50 et 7 pax) : 9272.60€\nHébergement (7 pax) : 3749.20€" },
                        { desc: "Le Mans : Zoo de Beauval", price: 11745.44, subDesc: "Location salle & Accès zoo : 4208.73€\nRestauration (80 et 7 pax) : 5384.28€\nAgent de sécurité : 216.67\nHébergement (7 pax) : 1613.29€" },
                        { desc: "Reims : G.H. Mumm", price: 21014.41, subDesc: "Location salle & Privatisation : 3333.20€\nRestauration : Accueil & Cocktail (80 pax), Dîner (7 pax) : 15999.11€\nHébergement (7 pax) : 1662.85€" }
                    ],
                    logistique: [
                        { desc: "Plateforme de gestion et inscriptions", price: 8520.40, subDesc: "Plateforme, e-mailing, SMS, Enquête satisfaction & Badges" },
                        { desc: "Signalétique", price: 2160.00, subDesc: "4 rolls up et 4 oriflammes, avec création graphique" },
                        { desc: "Acheminement et transferts", price: 8987.44, subDesc: "Transports en train et véhicules avec chauffeur" },
                        { desc: "Accueil sur sites", price: 610.14, subDesc: "Hôtesses d'accueil sur les différents sites" },
                        { desc: "Gestion des véhicules", price: 357.50, subDesc: "Péages et carburant" }
                    ],
                    frais_annexes: [
                        { desc: "Hébergement Staff (VHR)", price: 2080.00, subDesc: "4 nuitées pour 2 Weevers" },
                        { desc: "Restauration Staff (VHR)", price: 936.00, subDesc: "2 repas pour 4 Weevers (24 repas)" },
                        { desc: "Déplacements Staff (VHR)", price: 1642.22, subDesc: "Taxi, véhicules de location et trains" }
                    ]
                }
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

        const textColors = {
            personnel: "text-blue-500",
            technique: "text-purple-500",
            lieux: "text-orange-500",
            logistique: "text-slate-500",
            frais_annexes: "text-teal-500"
        };

        // --- UTILS ---
        const formatEur = (value) => {
            return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(value);
        };

        // --- COMPONENTS ---

        // Icons
        const IconBuilding = () => <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01"></path><path d="M16 6h.01"></path><path d="M12 6h.01"></path><path d="M12 10h.01"></path><path d="M12 14h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path></svg>;
        const IconChart = () => <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><path d="M3 9h18"></path><path d="M9 21V9"></path></svg>;

        const ComparisonView = () => {
            const venues = Object.values(budgetData);

            // Sort venues by total price (ascending) to find the cheapest
            const sortedVenues = [...venues].sort((a, b) => a.totalHT - b.totalHT);
            const maxTotalHT = Math.max(...venues.map(v => v.totalHT));

            return (
                <div className="space-y-8 animate-fade-in">

                    {/* Top KPI Cards */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {venues.map((venue) => {
                            return (
                                <div key={venue.id} className="relative bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                                    <h3 className="text-lg font-semibold text-gray-900 mb-4">{venue.name}</h3>
                                    <div className="mb-2">
                                        <p className="text-sm text-gray-500 uppercase tracking-wide">Budget Total TTC</p>
                                        <p className="text-3xl font-bold text-gray-900">{formatEur(venue.totalTTC)}</p>
                                    </div>
                                    <div className="flex justify-between text-sm text-gray-500 mt-4 pt-4 border-t border-gray-100">
                                        <span>Total HT: {formatEur(venue.totalHT)}</span>
                                    </div>
                                </div>
                            );
                        })}
                    </div>

                    {/* Visual Bar Chart */}
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                        <h3 className="text-lg font-semibold text-gray-900 mb-6">Répartition par catégorie (HT)</h3>

                        <div className="space-y-6">
                            {venues.map(venue => (
                                <div key={venue.id}>
                                    <div className="flex justify-between text-sm font-medium mb-2">
                                        <span>{venue.name}</span>
                                        <span>{formatEur(venue.totalHT - venue.honorairesHT)} HT <span className="text-gray-400 font-normal">(hors honoraires)</span></span>
                                    </div>
                                    {/* Stacked Bar Container */}
                                    <div className="h-6 w-full bg-gray-100 rounded-full overflow-hidden flex">
                                        {Object.entries(venue.categories).map(([catKey, catValue]) => {
                                            const percentage = (catValue / maxTotalHT) * 100;
                                            return (
                                                <div
                                                    key={catKey}
                                                    className={`h-full ${categoryColors[catKey]} group relative cursor-pointer border-r border-white/20 last:border-0`}
                                                    style={{ width: `${percentage}%` }}
                                                >
                                                    {/* Tooltip */}
                                                    <div className="absolute bottom-full mb-2 left-1/2 transform -translate-x-1/2 bg-gray-900 text-white text-xs rounded py-1 px-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-10 whitespace-nowrap">
                                                        {categoryLabels[catKey]}: {formatEur(catValue)} HT
                                                        <svg className="absolute text-gray-900 h-2 w-full left-0 top-full" x="0px" y="0px" viewBox="0 0 255 255"><polygon className="fill-current" points="0,0 127.5,127.5 255,0" /></svg>
                                                    </div>
                                                </div>
                                            );
                                        })}
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/* Legend */}
                        <div className="mt-6 flex flex-wrap gap-4 pt-4 border-t border-gray-100">
                            {Object.entries(categoryLabels).map(([key, label]) => (
                                <div key={key} className="flex items-center text-xs text-gray-600">
                                    <span className={`w-3 h-3 rounded-full mr-2 ${categoryColors[key]}`}></span>
                                    {label}
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Detailed Data Table */}
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
                        <div className="overflow-x-auto">
                            <table className="min-w-full divide-y divide-gray-200 text-sm">
                                <thead className="bg-gray-50">
                                    <tr>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Poste de Dépense (HT)</th>
                                        {venues.map(venue => (
                                            <th key={`th-${venue.id}`} className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">{venue.name}</th>
                                        ))}
                                    </tr>
                                </thead>
                                <tbody className="bg-white divide-y divide-gray-200">
                                    {Object.keys(categoryLabels).map(catKey => {
                                        // Find minimum value in this category to highlight it
                                        const values = venues.map(v => v.categories[catKey] || 0);
                                        const minVal = Math.min(...values);

                                        return (
                                            <tr key={catKey} className="hover:bg-gray-50 transition-colors">
                                                <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900 flex items-center">
                                                    <span className={`w-2 h-2 rounded-full mr-2 ${categoryColors[catKey]}`}></span>
                                                    {categoryLabels[catKey]}
                                                </td>
                                                {venues.map(venue => {
                                                    const val = venue.categories[catKey] || 0;
                                                    const isMin = val === minVal && venues.length > 1; // Only highlight if more than 1 venue
                                                    return (
                                                        <td key={`${catKey}-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right ${isMin ? 'text-green-600 font-semibold' : 'text-gray-600'}`}>
                                                            {formatEur(val)}
                                                        </td>
                                                    );
                                                })}
                                            </tr>
                                        )
                                    })}

                                    {/* Honoraires Row */}
                                    <tr className="bg-gray-50 border-t-2 border-gray-200">
                                        <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Honoraires Agence</td>
                                        {venues.map(venue => (
                                            <td key={`hon-${venue.id}`} className="px-6 py-4 whitespace-nowrap text-right text-gray-600">
                                                {formatEur(venue.honorairesHT)}
                                            </td>
                                        ))}
                                    </tr>

                                    {/* Totals Row TTC */}
                                    <tr className="bg-sky-50 border-t border-sky-200">
                                        <td className="px-6 py-4 whitespace-nowrap font-bold text-sky-900">TOTAL TTC</td>
                                        {venues.map(venue => {
                                            const isCheapest = venue.id === sortedVenues[0].id && venues.length > 1;
                                            return (
                                                <td key={`tot-ttc-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right font-bold text-lg ${isCheapest ? 'text-green-600' : 'text-sky-900'}`}>
                                                    {formatEur(venue.totalTTC)}
                                                </td>
                                            );
                                        })}
                                    </tr>

                                    {/* Sub Totals Row HT */}
                                    <tr className="bg-sky-50/50">
                                        <td className="px-6 py-3 whitespace-nowrap text-sm text-sky-700">Total HT</td>
                                        {venues.map(venue => (
                                            <td key={`tot-ht-${venue.id}`} className="px-6 py-3 whitespace-nowrap text-right text-sm text-sky-700">
                                                {formatEur(venue.totalHT)}
                                            </td>
                                        ))}
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>
            );
        };

        const VenueDetailView = ({ venueId }) => {
            const venue = budgetData[venueId];
            const subtotalHT = venue.totalHT - venue.honorairesHT;

            return (
                <div className="space-y-6 animate-fade-in">

                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">{venue.name}</h2>
                            <p className="text-gray-500">Détail du devis estimatif</p>
                        </div>
                        <div className="text-right bg-sky-50 p-4 rounded-lg border border-sky-100">
                            <p className="text-sm font-medium text-sky-600 uppercase tracking-wider mb-1">Total TTC</p>
                            <p className="text-3xl font-bold text-sky-900">{formatEur(venue.totalTTC)}</p>
                            <p className="text-xs text-sky-500 mt-1">Total HT: {formatEur(venue.totalHT)}</p>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                        {/* List Breakdown */}
                        <div className="lg:col-span-2 space-y-4">
                            {Object.entries(venue.categories).map(([catKey, catValue]) => {
                                const percentage = ((catValue / subtotalHT) * 100).toFixed(1);
                                return (
                                    <div key={catKey} className="bg-white rounded-lg shadow-sm border border-gray-200 p-4 flex flex-col gap-4">
                                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                            <div className="flex items-center gap-3">
                                                <div className={`min-w-[3.5rem] px-2 h-10 rounded-lg flex items-center justify-center text-white ${categoryColors[catKey]}`}>
                                                    <span className="font-bold text-sm">{percentage}%</span>
                                                </div>
                                                <div>
                                                    <h4 className="font-semibold text-gray-900">{categoryLabels[catKey]}</h4>
                                                    <div className="w-48 bg-gray-200 rounded-full h-1.5 mt-2">
                                                        <div className={`${categoryColors[catKey]} h-1.5 rounded-full`} style={{ width: `${percentage}%` }}></div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="text-right">
                                                <p className="text-lg font-bold text-gray-900">{formatEur(catValue)}</p>
                                                <p className="text-xs text-gray-500">HT</p>
                                            </div>
                                        </div>

                                        {/* Lignes de détail */}
                                        {venue.details && venue.details[catKey] && (
                                            <div className="mt-2 pt-4 border-t border-gray-100 space-y-3">
                                                {venue.details[catKey].map((item, idx) => (
                                                    <div key={idx} className="flex flex-col text-sm border-b border-gray-50 pb-2 last:border-0 last:pb-0">
                                                        <div className="flex justify-between items-start gap-4">
                                                            <span className="text-gray-800 font-medium">{item.desc}</span>
                                                            <span className="text-gray-900 font-bold whitespace-nowrap">{formatEur(item.price)}</span>
                                                        </div>
                                                        {item.subDesc && (
                                                            <div className="text-gray-500 text-xs mt-1 italic leading-relaxed whitespace-pre-line pr-16">
                                                                {item.subDesc}
                                                            </div>
                                                        )}
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                );
                            })}

                            <div className="bg-gray-50 rounded-lg border border-gray-200 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                <div>
                                    <h4 className="font-semibold text-gray-900">Honoraires de gestion</h4>
                                    <p className="text-sm text-gray-500">Honoraires Weever</p>
                                </div>
                                <div className="text-right">
                                    <p className="text-lg font-bold text-gray-900">{formatEur(venue.honorairesHT)}</p>
                                    <p className="text-xs text-gray-500">HT</p>
                                </div>
                            </div>
                        </div>

                        {/* Summary Box */}
                        <div className="lg:col-span-1">
                            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 sticky top-24">
                                <h3 className="text-lg font-semibold text-gray-900 mb-4 border-b pb-2">Récapitulatif Financier</h3>
                                <div className="space-y-3 text-sm">
                                    <div className="flex justify-between text-gray-600">
                                        <span>Sous-total HT</span>
                                        <span>{formatEur(subtotalHT)}</span>
                                    </div>
                                    <div className="flex justify-between text-gray-600">
                                        <span>Honoraires HT</span>
                                        <span>{formatEur(venue.honorairesHT)}</span>
                                    </div>
                                    <div className="border-t pt-3 flex justify-between text-gray-500 text-sm">
                                        <span>Total HT</span>
                                        <span>{formatEur(venue.totalHT)}</span>
                                    </div>
                                    <div className="flex justify-between text-gray-500 text-sm mt-1">
                                        <span>TVA estimée</span>
                                        <span>{formatEur(venue.totalTTC - venue.totalHT)}</span>
                                    </div>
                                    <div className="border-t pt-3 mt-2 flex justify-between font-bold text-sky-600 text-lg">
                                        <span>Total TTC</span>
                                        <span>{formatEur(venue.totalTTC)}</span>
                                    </div>
                                </div>

                                <div className="mt-6 bg-blue-50 text-blue-800 text-xs p-3 rounded border border-blue-100">
                                    <strong>Note:</strong> Les montants indiqués (notamment les transports) sont provisionnels et seront ajustés au réel.
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            );
        };

        function App() {
            const [activeTab, setActiveTab] = useState('compare');

            return (
                <div className="min-h-screen bg-slate-50 pb-12 font-sans">
                    {/* Header */}
                    <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
                        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
                            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                                <div>
                                    <h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                                        <span className="text-yellow-500">☀️</span> Volkswagen Bank — Séminaire 2026
                                    </h1>
                                    <p className="text-sm text-gray-500">Vue synthèse et détaillée des Tournées Régionales</p>
                                </div>

                                {/* Navigation Tabs */}
                                <div className="flex space-x-1 bg-gray-100 p-1 rounded-lg overflow-x-auto">
                                    <button
                                        onClick={() => setActiveTab('compare')}
                                        className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${activeTab === 'compare' ? 'bg-white text-sky-600 shadow-sm' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-200'}`}
                                    >
                                        <IconChart /> Vue Synthèse
                                    </button>
                                    {Object.values(budgetData).map(venue => (
                                        <button
                                            key={venue.id}
                                            onClick={() => setActiveTab(venue.id)}
                                            className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${activeTab === venue.id ? 'bg-white text-sky-600 shadow-sm' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-200'}`}
                                        >
                                            <IconBuilding /> {venue.name}
                                        </button>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </header>

                    {/* Main Content */}
                    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8">
                        {activeTab === 'compare' ? <ComparisonView /> : <VenueDetailView venueId={activeTab} />}
                    </main>
                </div>
            );
        }

        // Mount the app
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>

</html>
"""

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "w", encoding="utf-8") as f:
    f.write(html_content)
