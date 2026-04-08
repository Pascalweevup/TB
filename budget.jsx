import React, { useState } from 'react';

// --- DATA EXTRACTED FROM PDFs V2 ---
const budgetData = {
    bnf: { 
        id: 'bnf',
        name: "BNF", 
        totalTTC: 129807.11, 
        totalHT: 108265.54, 
        honorairesHT: 9842.32, 
        categories: { 
            lieux: 32768.16, 
            restauration: 27350.69, 
            technique: 11521.87, 
            transports: 7800.00, 
            extras: 14667.50, 
            accompagnement: 4315.00 
        },
        details: {
            lieux: [
                { desc: "Location de salle ateliers Marriott Rive Gauche (3 salles)", price: 7840.91 },
                { desc: "Location de salle cérémonie et cocktail BNF", price: 8125.00 },
                { desc: "Nuitées Marriott Rive Gauche (60 pax)", price: 16295.25 },
                { desc: "Taxe de séjour Marriott Rive Gauche (60 pax)", price: 507.00 }
            ],
            restauration: [
                { desc: "Déjeuner d'équipe Bistrot Palyma", price: 732.94 },
                { desc: "Café d'accueil ateliers Marriott Rive Gauche", price: 1023.00 },
                { desc: "Pause café ateliers Marriott Rive Gauche", price: 1363.50 },
                { desc: "Cocktail dînatoire - repas Les Retraiteurs", price: 11750.00 },
                { desc: "Cocktail dînatoire - boissons softs", price: 1050.00 },
                { desc: "Cocktail dînatoire - boissons alcoolisées", price: 4818.75 },
                { desc: "Cocktail dînatoire - Mobilier", price: 6612.50 }
            ],
            technique: [
                { desc: "Audiovisuel", price: 7907.50 },
                { desc: "Forfait mobilier scénique", price: 0.00 },
                { desc: "Mobilier scénique : étagère trophées", price: 961.87 },
                { desc: "Agent de sécurité", price: 250.00 },
                { desc: "Hôtes(ses)", price: 1750.00 },
                { desc: "Matériel de vestiaire", price: 300.00 },
                { desc: "Frais de personnel heure de jour", price: 80.00 },
                { desc: "Frais de personnel heure de nuit", price: 122.50 },
                { desc: "Transport de matériel", price: 150.00 },
                { desc: "Infographiste (Option)", price: 600.00 }
            ],
            transports: [
                { desc: "Provision transports", price: 6000.00 },
                { desc: "Frais de gestion des transports", price: 1800.00 }
            ],
            extras: [
                { desc: "Animation - performance Salt & Pepper", price: 10680.00 },
                { desc: "Animation - caricaturistes", price: 3562.50 },
                { desc: "Badges", price: 325.00 },
                { desc: "Création graphique", price: 100.00 },
                { desc: "Intervention Oldyssey (Option)", price: 2340.00 },
                { desc: "Cadeaux livres (Option)", price: 1027.00 },
                { desc: "Sac kraft (Option)", price: 212.50 }
            ],
            accompagnement: [
                { desc: "Temps homme Weever", price: 3600.00 },
                { desc: "VRH - Restauration", price: 120.00 },
                { desc: "VHR - Transport", price: 195.00 },
                { desc: "Frais de repérage", price: 400.00 }
            ]
        }
    },
    cirque: { 
        id: 'cirque',
        name: "Cirque d'Hiver", 
        totalTTC: 147841.00, 
        totalHT: 123261.66, 
        honorairesHT: 11205.61, 
        categories: { 
            lieux: 40191.73, 
            restauration: 25033.39, 
            technique: 26352.59, 
            transports: 7800.00, 
            extras: 8363.35, 
            accompagnement: 4315.00 
        },
        details: {
            lieux: [
                { desc: "Location de la verrière ateliers (Hôtel Provinces Opéra)", price: 252.08 },
                { desc: "Location de salles ateliers (4 salles, Hôtel Provinces Opéra)", price: 2016.68 },
                { desc: "Location de salle cérémonie et cocktail (Cirque d'Hiver)", price: 24200.00 },
                { desc: "Nuitée Chambre individuelle Confort (14 pax)", price: 3018.37 },
                { desc: "Nuitée Chambre individuelle Privilège (6 pax)", price: 1352.97 },
                { desc: "Nuitée Chambre double Confort à usage individuel (40 pax)", price: 9019.82 },
                { desc: "Taxe de séjour (60 pax)", price: 331.80 }
            ],
            restauration: [
                { desc: "Déjeuner d'équipe Hôtel Provinces Opéra", price: 527.98 },
                { desc: "Café d'accueil ateliers", price: 395.67 },
                { desc: "Pause gourmande ateliers", price: 659.93 },
                { desc: "Cocktail dînatoire - repas et softs", price: 10285.00 },
                { desc: "Cocktail dînatoire - boissons alcoolisées", price: 653.40 },
                { desc: "Cocktail - matériel et logistique", price: 5033.60 },
                { desc: "Cocktail - personnel de service", price: 5783.80 },
                { desc: "Cocktail - champagne", price: 1694.00 },
                { desc: "Cocktail - ateliers culinaires (Option)", price: 3388.00 }
            ],
            technique: [
                { desc: "Consommation gaz/électricité", price: 605.00 },
                { desc: "Toiles tendues (Option)", price: 2420.00 },
                { desc: "Projection sur toiles tendues (Option)", price: 1562.11 },
                { desc: "Forfait technique sonorisation et lumières", price: 13631.86 },
                { desc: "Forfait technique vidéo", price: 6688.28 },
                { desc: "Forfait mobilier scénique", price: 0.00 },
                { desc: "Mobilier scénique : étagère trophées", price: 961.87 },
                { desc: "Réseau wifi (Option)", price: 3388.00 },
                { desc: "Transport de matériel", price: 150.00 },
                { desc: "Equipe de sécurité", price: 1060.69 },
                { desc: "Hôtes(ses) vestiaire et accueil", price: 2662.00 },
                { desc: "Matériel vestiaire", price: 592.90 },
                { desc: "Infographiste (Option)", price: 600.00 }
            ],
            transports: [
                { desc: "Provision transports", price: 6000.00 },
                { desc: "Frais de gestion des transports", price: 1800.00 }
            ],
            extras: [
                { desc: "Animation numéro de Cirque n°1", price: 3630.00 },
                { desc: "Animation numéro de Cirque n°2 (Option)", price: 3630.00 },
                { desc: "Animation groupe musical (Jazz New Orleans)", price: 2420.00 },
                { desc: "Badges", price: 325.00 },
                { desc: "Création graphique", price: 100.00 },
                { desc: "Cadeaux - Cartes à jouer", price: 1675.85 },
                { desc: "Sac kraft", price: 212.50 }
            ],
            accompagnement: [
                { desc: "Temps homme Weever", price: 3600.00 },
                { desc: "VRH - Restauration", price: 120.00 },
                { desc: "VHR - Transport", price: 195.00 },
                { desc: "Frais de repérage", price: 400.00 }
            ]
        }
    }
};

const categoryLabels = {
    lieux: "Lieux & Hébergement",
    restauration: "Restauration",
    technique: "Technique",
    transports: "Transports",
    extras: "Extras & Animations",
    accompagnement: "Accompagnement (Weever)"
};

// Utilisation des couleurs standard Tailwind au lieu d'une configuration personnalisée
const categoryColors = {
    lieux: "bg-blue-500",
    restauration: "bg-orange-500",
    technique: "bg-purple-500",
    transports: "bg-slate-500",
    extras: "bg-pink-500",
    accompagnement: "bg-teal-500"
};

const textColors = {
    lieux: "text-blue-500",
    restauration: "text-orange-500",
    technique: "text-purple-500",
    transports: "text-slate-500",
    extras: "text-pink-500",
    accompagnement: "text-teal-500"
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
                                <p className="text-sm text-gray-500 uppercase tracking-wide">Budget Total HT</p>
                                <p className="text-3xl font-bold text-gray-900">{formatEur(venue.totalHT)}</p>
                            </div>
                            <div className="flex justify-between text-sm text-gray-500 mt-4 pt-4 border-t border-gray-100">
                                <span>Total TTC: {formatEur(venue.totalTTC)}</span>
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
                                                <svg className="absolute text-gray-900 h-2 w-full left-0 top-full" x="0px" y="0px" viewBox="0 0 255 255"><polygon className="fill-current" points="0,0 127.5,127.5 255,0"/></svg>
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
                                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">BNF</th>
                                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Cirque d'Hiver</th>
                            </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                            {Object.keys(categoryLabels).map(catKey => {
                                // Find minimum value in this category to highlight it
                                const values = venues.map(v => v.categories[catKey]);
                                const minVal = Math.min(...values);

                                return (
                                    <tr key={catKey} className="hover:bg-gray-50 transition-colors">
                                        <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900 flex items-center">
                                            <span className={`w-2 h-2 rounded-full mr-2 ${categoryColors[catKey]}`}></span>
                                            {categoryLabels[catKey]}
                                        </td>
                                        {venues.map(venue => {
                                            const val = venue.categories[catKey];
                                            const isMin = val === minVal;
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
                            <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Honoraires Agence (10%)</td>
                            {venues.map(venue => (
                                <td key={`hon-${venue.id}`} className="px-6 py-4 whitespace-nowrap text-right text-gray-600">
                                    {formatEur(venue.honorairesHT)}
                                </td>
                            ))}
                        </tr>
                        
                        {/* Totals Row HT */}
                        <tr className="bg-sky-50 border-t border-sky-200">
                            <td className="px-6 py-4 whitespace-nowrap font-bold text-sky-900">TOTAL HT</td>
                            {venues.map(venue => {
                                const isCheapest = venue.id === sortedVenues[0].id;
                                return (
                                    <td key={`tot-ht-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right font-bold text-lg ${isCheapest ? 'text-green-600' : 'text-sky-900'}`}>
                                        {formatEur(venue.totalHT)}
                                    </td>
                                );
                            })}
                        </tr>
                        
                        {/* Sub Totals Row TTC */}
                        <tr className="bg-sky-50/50">
                            <td className="px-6 py-3 whitespace-nowrap text-sm text-sky-700">Total TTC</td>
                            {venues.map(venue => (
                                <td key={`tot-ttc-${venue.id}`} className="px-6 py-3 whitespace-nowrap text-right text-sm text-sky-700">
                                    {formatEur(venue.totalTTC)}
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
                    <p className="text-sm font-medium text-sky-600 uppercase tracking-wider mb-1">Total HT</p>
                    <p className="text-3xl font-bold text-sky-900">{formatEur(venue.totalHT)}</p>
                    <p className="text-xs text-sky-500 mt-1">Total TTC: {formatEur(venue.totalTTC)}</p>
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
                                
                                {/* Lignes de détail ajoutées ici */}
                                {venue.details && venue.details[catKey] && (
                                    <div className="mt-2 pt-4 border-t border-gray-100 space-y-2">
                                        {venue.details[catKey].map((item, idx) => (
                                            <div key={idx} className="flex justify-between items-end text-sm">
                                                <span className="text-gray-600">{item.desc}</span>
                                                <span className="text-gray-900 font-medium whitespace-nowrap ml-4">{formatEur(item.price)}</span>
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </div>
                        );
                    })}
                    
                    <div className="bg-gray-50 rounded-lg border border-gray-200 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <h4 className="font-semibold text-gray-900">Honoraires Weever (10%)</h4>
                            <p className="text-sm text-gray-500">Calculés sur le sous-total HT</p>
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
                            <div className="border-t pt-3 flex justify-between font-bold text-sky-600 text-lg">
                                <span>Total HT</span>
                                <span>{formatEur(venue.totalHT)}</span>
                            </div>
                            <div className="flex justify-between text-gray-500 text-sm mt-2">
                                <span>TVA estimée</span>
                                <span>{formatEur(venue.totalTTC - venue.totalHT)}</span>
                            </div>
                            <div className="flex justify-between text-gray-500 text-sm">
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

export default function App() {
    const [activeTab, setActiveTab] = useState('compare');

    return (
        <div className="min-h-screen bg-slate-50 pb-12 font-sans">
            {/* Header */}
            <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
                    <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div>
                            <h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                                <span className="text-yellow-500">☀️</span> Atout Soleil 2026
                            </h1>
                            <p className="text-sm text-gray-500">Comparateur interactif de propositions événementielles</p>
                        </div>
                        
                        {/* Navigation Tabs */}
                        <div className="flex space-x-1 bg-gray-100 p-1 rounded-lg overflow-x-auto">
                            <button 
                                onClick={() => setActiveTab('compare')}
                                className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${activeTab === 'compare' ? 'bg-white text-sky-600 shadow-sm' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-200'}`}
                            >
                                <IconChart /> Vue Comparée
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
