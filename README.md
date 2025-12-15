# PDF Document Extractor (Python)

Mini engine to extract structured data from real-world PDF documents
(quotes / invoices) and send clean JSON to Make for automation (e.g. Monday).

## Features
- Document type detection
- Email extraction
- Phone extraction
- Date extraction
- Total HT extraction (robust to real PDF quirks)
- Webhook integration (Make)

## Run locally
```bash
python src/main.py
python src/send_to_make.py
