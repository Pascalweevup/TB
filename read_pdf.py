import subprocess
import sys

try:
    import PyPDF2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

filename = "/Users/lolaricharte/Documents/Atout Soleil/Atout/Volks-budget/7 - ANNEXE 1_RFP_VWBK_Tournées_Régionales_2026_Offre financière.xlsx - Offre - Details.pdf"
try:
    reader = PyPDF2.PdfReader(filename)
    with open("pdf_text.txt", "w") as f:
        for i in range(len(reader.pages)):
            f.write(f"--- Page {i} ---\n")
            f.write(reader.pages[i].extract_text() + "\n")
except Exception as e:
    with open("pdf_text.txt", "w") as f:
        f.write(f"Error reading PDF: {e}")
