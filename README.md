<div align="center">

# 📄 PDF Page Counter

### 📊 Genera un Report Excel dai tuoi PDF in un click

Uno strumento essenziale per archivisti e amministratori.  
Analizza una directory, conta le pagine dei PDF e organizza tutto in un foglio Excel.

<br />

✨ Funzionalità • 📦 Requisiti • 🛠️ Installazione • ⚙️ Configurazione • 📊 Output

</div>

---

## 🚀 Funzionalità

Dimentica il conteggio manuale. Questo script automatizza la catalogazione dei documenti.

- 🔍 **Scansione Directory**: Analizza tutti i file `.pdf` presenti in una cartella specificata.
- 🔢 **Conteggio Pagine**: Apre ogni PDF ed estrae il numero esatto di pagine.
- 📑 **Report Excel**: Genera un file `.xlsx` pulito e ordinato.
- 🛡️ **Gestione Errori**: Ignora file corrotti o non leggibili senza interrompere l'esecuzione.

> ⚠️ Nota: Lo script analizza solo i PDF presenti nella cartella indicata (non nelle sottocartelle).

---

## 📦 Requisiti

Assicurati di avere:

- Python 3.x
- Librerie Python:
  - `openpyxl` → gestione file Excel
  - `PyPDF2` → lettura e parsing PDF

---

## 🛠️ Installazione

### 1️⃣ Clona il repository

```bash
git clone https://github.com/tuo-username/pdf-page-counter.git
cd pdf-page-counter
```

### 2️⃣ Installa le dipendenze

```bash
pip install openpyxl PyPDF2
```

## ⚙️ Configurazione
Prima di eseguire lo script, modifica le variabili nel file .py:

```Python
# 📂 CONFIGURAZIONE PERCORSI

# Cartella contenente i PDF da analizzare
percorso_cartella = r"C:\Utenti\TuoNome\Documenti\MieiPDF"

# Percorso completo per il salvataggio del report Excel
output_excel = r"C:\Utenti\TuoNome\Desktop\report_pagine.xlsx"
```
## ▶️ Utilizzo

Esegui lo script dal terminale:
```Python
python nome_script.py
```
Al termine dell’elaborazione troverai il file Excel nel percorso specificato.

## 📊 Esempio di Output

Il file Excel generato avrà una struttura come questa:
| 📄 Nome File           | 🔢 Pagine |
| ---------------------- | --------- |
| documento_progetto.pdf | 10        |
| fattura_2023.pdf       | 3         |
| manuale_utente.pdf     | 25        |
| scansione_veloce.pdf   | 1         |

<div align="center">

<sub>Creato per semplificare la gestione documentale.</sub>
<br />
<sub>Se ti è stato utile, lascia una ⭐ al repository.</sub>

</div> ```
