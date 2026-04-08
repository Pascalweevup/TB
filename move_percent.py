import os

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the title cell in the data table to contain the pill
old_title_cell = """                                                <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900 flex items-center">
                                                    <span className={`w-2 h-2 rounded-full mr-2 ${categoryColors[catKey]}`}></span>
                                                    {categoryLabels[catKey]}
                                                </td>"""

new_title_cell = """                                                <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900 flex items-center gap-3">
                                                    {(()=>{
                                                        const venue = venues[0];
                                                        const val = venue.categories[catKey] || 0;
                                                        const subtotalHT = venue.totalHT - venue.honorairesHT;
                                                        const percentage = subtotalHT > 0 ? ((val / subtotalHT) * 100).toFixed(1) : 0;
                                                        return (
                                                            <div className={`px-2 py-1 rounded-md text-white text-xs font-bold ${categoryColors[catKey]}`}>
                                                                {percentage}%
                                                            </div>
                                                        );
                                                    })()}
                                                    {categoryLabels[catKey]}
                                                </td>"""

# 2. Revert the price cell to remove the percentage under the price
old_price_cell = """                                                {venues.map(venue => {
                                                    const val = venue.categories[catKey] || 0;
                                                    const subtotalHT = venue.totalHT - venue.honorairesHT;
                                                    const percentage = subtotalHT > 0 ? ((val / subtotalHT) * 100).toFixed(1) : 0;
                                                    const isMin = val === minVal && venues.length > 1; // Only highlight if more than 1 venue
                                                    return (
                                                        <td key={`${catKey}-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right ${isMin ? 'text-green-600 font-semibold' : 'text-gray-600'}`}>
                                                            <div>{formatEur(val)}</div>
                                                            <div className="text-xs text-gray-400 font-normal mt-0.5">{percentage}%</div>
                                                        </td>
                                                    );
                                                })}"""

new_price_cell = """                                                {venues.map(venue => {
                                                    const val = venue.categories[catKey] || 0;
                                                    const isMin = val === minVal && venues.length > 1; // Only highlight if more than 1 venue
                                                    return (
                                                        <td key={`${catKey}-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right ${isMin ? 'text-green-600 font-semibold' : 'text-gray-600'}`}>
                                                            {formatEur(val)}
                                                        </td>
                                                    );
                                                })}"""

if old_title_cell in html:
    html = html.replace(old_title_cell, new_title_cell)
else:
    print("Warning: old title cell not found strings")

if old_price_cell in html:
    html = html.replace(old_price_cell, new_price_cell)
else:
    print("Warning: old price cell not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
