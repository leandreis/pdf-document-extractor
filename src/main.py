import pdfplumber
import json

from fields import (
    extract_document_type,
    extract_emails,
    extract_phones,
    extract_dates,
    extract_total_ht
)

PDF_PATH = "data/sample.pdf"

def run():
    with pdfplumber.open(PDF_PATH) as pdf:
        text = "\n".join(
            page.extract_text() or ""
            for page in pdf.pages
        )
        page_count = len(pdf.pages)

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    result = {
        "page_count": page_count,
        "line_count": len(lines),
        "document_type": extract_document_type(lines),
        "emails": extract_emails(lines),
        "phones": extract_phones(lines),
        "dates": extract_dates(lines),
        "total_ht": extract_total_ht(lines),
    }


    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Extraction saved to output.json")



if __name__ == "__main__":
    run()
