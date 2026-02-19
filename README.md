📄 PDF Page Counter → Excel Report

Questo script Python scansiona una cartella contenente file PDF e genera automaticamente un file Excel con:

📌 Nome del file PDF

📌 Numero di pagine di ciascun PDF

È utile per creare rapidamente un report riepilogativo dei documenti presenti in una directory.

⚙️ Come funziona

Lo script legge tutti i file .pdf presenti nella cartella indicata.

Per ogni file:

Apre il PDF

Conta il numero di pagine usando PyPDF2

Scrive i risultati in un file Excel usando openpyxl

Salva il file Excel nel percorso specificato.

📦 Requisiti

Python 3.x

Librerie necessarie:

pip install openpyxl PyPDF2

🛠 Configurazione

Nel file Python modifica questa riga inserendo il percorso della cartella che contiene i PDF:

percorso_cartella = r"C:\percorso\della\tua\cartella"


E, se necessario, modifica il nome o il percorso del file Excel di output:

output_excel = r"C:\percorso\di\salvataggio\report_pagine.xlsx"

▶️ Esecuzione

Esegui lo script con:

python nome_script.py


Al termine verrà creato un file Excel con l’elenco dei PDF e il numero di pagine.
