import re

def extract_invoice_data(text: str) -> dict:
    invoice_number = re.search(r'(FAC[-\s]?\d+)', text)
    date = re.search(r'(\d{2}/\d{2}/\d{4})', text)
    total = re.search(r'TTC\s*[:\-]?\s*([\d\s,\.]+)', text)
    supplier = re.search(r'Société\s+([A-Za-z0-9\s]+)', text)

    return {
        "invoice_number": invoice_number.group(1) if invoice_number else None,
        "invoice_date": date.group(1) if date else None,
        "total_amount": float(total.group(1).replace(' ', '').replace(',', '.')) if total else None,
        "supplier_name": supplier.group(1).strip() if supplier else None
    }