import os

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Top KPI Cards in ComparisonView
old_kpi = """                                    <div className="mb-2">
                                        <p className="text-sm text-gray-500 uppercase tracking-wide">Budget Total TTC</p>
                                        <p className="text-3xl font-bold text-gray-900">{formatEur(venue.totalTTC)}</p>
                                    </div>
                                    <div className="flex justify-between text-sm text-gray-500 mt-4 pt-4 border-t border-gray-100">
                                        <span>Total HT: {formatEur(venue.totalHT)}</span>
                                    </div>"""

new_kpi = """                                    <div className="mb-2">
                                        <p className="text-sm text-gray-500 uppercase tracking-wide">Budget Total HT</p>
                                        <p className="text-3xl font-bold text-gray-900">{formatEur(venue.totalHT)}</p>
                                    </div>"""
html = html.replace(old_kpi, new_kpi)

# 2. Update Totals in Data Table (ComparisonView)
old_table_totals = """                                    {/* Totals Row TTC */}
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
                                    </tr>"""

new_table_totals = """                                    {/* Totals Row HT */}
                                    <tr className="bg-sky-50 border-t border-sky-200">
                                        <td className="px-6 py-4 whitespace-nowrap font-bold text-sky-900">Total HT</td>
                                        {venues.map(venue => {
                                            const isCheapest = venue.id === sortedVenues[0].id && venues.length > 1;
                                            return (
                                                <td key={`tot-ht-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right font-bold text-lg ${isCheapest ? 'text-green-600' : 'text-sky-900'}`}>
                                                    {formatEur(venue.totalHT)}
                                                </td>
                                            );
                                        })}
                                    </tr>"""
html = html.replace(old_table_totals, new_table_totals)


# 3. Update top banner in VenueDetailView
old_venue_top = """                        <div className="text-right bg-sky-50 p-4 rounded-lg border border-sky-100">
                            <p className="text-sm font-medium text-sky-600 uppercase tracking-wider mb-1">Total TTC</p>
                            <p className="text-3xl font-bold text-sky-900">{formatEur(venue.totalTTC)}</p>
                            <p className="text-xs text-sky-500 mt-1">Total HT: {formatEur(venue.totalHT)}</p>
                        </div>"""
new_venue_top = """                        <div className="text-right bg-sky-50 p-4 rounded-lg border border-sky-100">
                            <p className="text-sm font-medium text-sky-600 uppercase tracking-wider mb-1">Total HT</p>
                            <p className="text-3xl font-bold text-sky-900">{formatEur(venue.totalHT)}</p>
                        </div>"""
html = html.replace(old_venue_top, new_venue_top)


# 4. Update Summary Box in VenueDetailView
old_summary_box = """                                    <div className="border-t pt-3 flex justify-between text-gray-500 text-sm">
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
                                    </div>"""
new_summary_box = """                                    <div className="border-t border-sky-200 pt-3 flex justify-between font-bold text-sky-600 text-lg">
                                        <span>Total HT</span>
                                        <span>{formatEur(venue.totalHT)}</span>
                                    </div>"""
html = html.replace(old_summary_box, new_summary_box)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
