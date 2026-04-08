import os

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update (hors honoraires) string in ComparisonView stacked bars
old_hors_honoraires = """                                        <span>{formatEur(venue.totalHT - venue.honorairesHT)} HT <span className="text-gray-400 font-normal">(hors honoraires)</span></span>"""
new_total_ht = """                                        <span>{formatEur(venue.totalHT)} HT</span>"""
html = html.replace(old_hors_honoraires, new_total_ht)

# 2. Update percentages calc in ComparisonView (title cells)
old_percent_cv = """                                                        const subtotalHT = venue.totalHT - venue.honorairesHT;
                                                        const percentage = subtotalHT > 0 ? ((val / subtotalHT) * 100).toFixed(1) : 0;"""
new_percent_cv = """                                                        const percentage = venue.totalHT > 0 ? ((val / venue.totalHT) * 100).toFixed(1) : 0;"""
html = html.replace(old_percent_cv, new_percent_cv)

# 3. Remove Honoraires Agence row in ComparisonView table
old_honoraire_row = """                                    {/* Honoraires Row */}
                                    <tr className="bg-gray-50 border-t-2 border-gray-200">
                                        <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Honoraires Agence</td>
                                        {venues.map(venue => (
                                            <td key={`hon-${venue.id}`} className="px-6 py-4 whitespace-nowrap text-right text-gray-600">
                                                {formatEur(venue.honorairesHT)}
                                            </td>
                                        ))}
                                    </tr>"""
html = html.replace(old_honoraire_row, "")

# 4. Update percentage calc in VenueDetailView
old_subtotal_vdv = """            const venue = budgetData[venueId];
            const subtotalHT = venue.totalHT - venue.honorairesHT;"""
new_subtotal_vdv = """            const venue = budgetData[venueId];"""
html = html.replace(old_subtotal_vdv, new_subtotal_vdv)

old_percent_vdv = """                            {Object.entries(venue.categories).map(([catKey, catValue]) => {
                                const percentage = ((catValue / subtotalHT) * 100).toFixed(1);"""
new_percent_vdv = """                            {Object.entries(venue.categories).map(([catKey, catValue]) => {
                                const percentage = ((catValue / venue.totalHT) * 100).toFixed(1);"""
html = html.replace(old_percent_vdv, new_percent_vdv)

# 5. Remove Honoraires Weever block in VenueDetailView
old_honoraire_block = """                            <div className="bg-gray-50 rounded-lg border border-gray-200 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                <div>
                                    <h4 className="font-semibold text-gray-900">Honoraires de gestion</h4>
                                    <p className="text-sm text-gray-500">Honoraires Weever</p>
                                </div>
                                <div className="text-right">
                                    <p className="text-lg font-bold text-gray-900">{formatEur(venue.honorairesHT)}</p>
                                    <p className="text-xs text-gray-500">HT</p>
                                </div>
                            </div>"""
html = html.replace(old_honoraire_block, "")

# 6. Remove Sous-total HT and Honoraires HT from VenueDetailView summary box
old_summary_items = """                                <div className="space-y-3 text-sm">
                                    <div className="flex justify-between text-gray-600">
                                        <span>Sous-total HT</span>
                                        <span>{formatEur(subtotalHT)}</span>
                                    </div>
                                    <div className="flex justify-between text-gray-600">
                                        <span>Honoraires HT</span>
                                        <span>{formatEur(venue.honorairesHT)}</span>
                                    </div>
                                    <div className="border-t border-sky-200 pt-3 flex justify-between font-bold text-sky-600 text-lg">"""
new_summary_items = """                                <div className="space-y-3 text-sm">
                                    <div className="border-t border-sky-200 pt-3 flex justify-between font-bold text-sky-600 text-lg">"""

# Wait, the summary box format might be slightly different. In revert_update:
old_summary_items_fallback_check = """<span>Sous-total HT</span>"""
if old_summary_items_fallback_check in html:
    html = html.replace(old_summary_items, new_summary_items)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
