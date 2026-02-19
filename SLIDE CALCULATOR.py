import os
import openpyxl
from PyPDF2 import PdfReader

def crea_excel_pdf(cartella, output_excel):
    """Crea un file Excel con titolo del file PDF e numero di pagine."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Lista PDF"
    
    # Intestazioni
    ws.append(["Nome File", "Pagine"])

    for file in os.listdir(cartella):
        if file.endswith(".pdf"):
            percorso_file = os.path.join(cartella, file)
            try:
                with open(percorso_file, "rb") as f:
                    reader = PdfReader(f)
                    num_pagine = len(reader.pages)
                    ws.append([file, num_pagine])  # Aggiunge i dati al foglio
            except Exception as e:
                print(f"Errore con {file}: {e}")

    # Salva il file Excel
    wb.save(output_excel)
    print(f"File Excel creato: {output_excel}")

# Imposta la cartella con i PDF e il nome del file Excel
percorso_cartella = r""  # Cambia con il tuo percorso
output_excel = r"C:\Users\tiber\OneDrive\Desktop\report_pagine.pdf.xlsx"  # Nome del file Excel di output

crea_excel_pdf(percorso_cartella, output_excel)
