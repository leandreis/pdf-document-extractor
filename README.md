# PDF Document Extraction & Automation (Python)

This project is a lightweight **document intelligence engine** built in Python.
It extracts structured business data from real-world PDF documents (quotes, invoices, cost sheets)
and sends clean JSON to automation workflows (Make, Monday.com, CRM).

---

## 🚀 What this project does

From a PDF document, the script reliably extracts:

- Document type (e.g. Quote / Invoice)
- Contact emails
- Phone numbers
- Relevant dates
- **Total HT (robust extraction from real PDFs)**
- Page and line metadata

The output is a clean, structured JSON ready to be consumed by automation tools.

---

## ⚠️ Why this matters (real-world PDFs are messy)

Most PDFs are not clean:
- non-breaking spaces
- inconsistent labels (e.g. *Total HT*, *Total général net HT*)
- amounts mixed with layout artifacts
- multiple dates and totals

This project handles those issues using **deterministic parsing logic**
before introducing any AI layer, ensuring **accuracy and reliability**.

---

## 🧠 Tech stack

- Python
- pdfplumber
- Regular Expressions (regex)
- JSON
- Make (webhook integration)
- Monday.com (downstream usage)

---

## 📦 Example output

```json
{
  "document_type": "DEVIS",
  "emails": ["contact@example.com"],
  "phones": ["06.00.00.87.99"],
  "dates": ["2024-08-05"],
  "total_ht": 1200.75
}

## 🔁 Automation flow

PDF → Python extraction → JSON → Make webhook → Monday / CRM

## ▶️ How to run locally
python src/main.py
python src/send_to_make.py


## 🧩 Possible extensions
- VAT & Total TTC extraction
- Confidence scoring per extracted field
- AI fallback for complex layouts
- Batch processing (multiple PDFs)
- REST API (FastAPI)

##🎯 Typical use cases
- Finance & cost automation
- CRM / ERP document ingestion
- Operations workflows
- AI & automation projects
