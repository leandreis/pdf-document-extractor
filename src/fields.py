import re

def extract_document_type(lines: list[str]) -> str | None:
    for line in lines:
        if line.isupper() and len(line) < 30:
            return line
    return None


def extract_emails(lines: list[str]) -> list[str]:
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return list(set(re.findall(pattern, " ".join(lines))))


def extract_phones(lines: list[str]) -> list[str]:
    pattern = r"(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}"
    return list(set(re.findall(pattern, " ".join(lines))))


def extract_dates(lines: list[str]) -> list[str]:
    pattern = r"\b\d{2}[./-]\d{2}[./-]\d{4}\b"
    return list(set(re.findall(pattern, " ".join(lines))))

def extract_total_ht(lines: list[str]) -> float | None:
    """
    Robust extraction of TOTAL HT from real-world French PDFs.
    """

    for line in lines:
        line_upper = line.upper()

        # On ignore les en-têtes de tableau
        if "CODE" in line_upper and "PRIX" in line_upper:
            continue

        if ("TOTAL" in line_upper or "NET" in line_upper) and "HT" in line_upper:

            # 🔑 Regex MONÉTAIRE stricte (oblige les décimales)
            match = re.search(
                r"(\d{1,3}(?:[\s\u00A0]\d{3})*,\d{2})\s*(?:€|EUR)?",
                line
            )

            if not match:
                continue

            amount_str = match.group(1)

            # Nettoyage format FR → float
            amount_str = (
                amount_str
                .replace("\u00A0", "")
                .replace(" ", "")
                .replace(",", ".")
            )

            try:
                return float(amount_str)
            except ValueError:
                continue

    return None



    return None
