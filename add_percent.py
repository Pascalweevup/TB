import os

path = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

old_table_cells = """                                                {venues.map(venue => {
                                                    const val = venue.categories[catKey] || 0;
                                                    const isMin = val === minVal && venues.length > 1; // Only highlight if more than 1 venue
                                                    return (
                                                        <td key={`${catKey}-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right ${isMin ? 'text-green-600 font-semibold' : 'text-gray-600'}`}>
                                                            {formatEur(val)}
                                                        </td>
                                                    );
                                                })}"""

new_table_cells = """                                                {venues.map(venue => {
                                                    const val = venue.categories[catKey] || 0;
                                                    const subtotalHT = venue.totalHT - venue.honorairesHT;
                                                    const percentage = subtotalHT > 0 ? ((val / subtotalHT) * 100).toFixed(1) : 0;
                                                    const isMin = val === minVal && venues.length > 1; // Only highlight if more than 1 venue
                                                    return (
                                                        <td key={`${catKey}-${venue.id}`} className={`px-6 py-4 whitespace-nowrap text-right flex flex-col items-end ${isMin ? 'text-green-600 font-semibold' : 'text-gray-600'}`}>
                                                            <span>{formatEur(val)}</span>
                                                            <span className="text-xs text-gray-400 font-normal">{percentage}% du refacturable</span>
                                                        </td>
                                                    );
                                                })}"""

# Wait, the `td` is `table-cell`. `flex flex-col` on a `td` might break the table cell alignment or it might work.
# Actually, just grouping inside a div or spans.
new_table_cells2 = """                                                {venues.map(venue => {
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
html = html.replace(old_table_cells, new_table_cells2)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
