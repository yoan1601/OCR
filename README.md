# Invoice OCR & Data Extraction API

This project provides a RESTful API for performing OCR (Optical Character Recognition) and automatic data extraction from supplier invoices (PDF or image format). The backend is implemented in Python using FastAPI and Tesseract, and is designed to be integrated with enterprise applications (such as .NET Framework 4.8 solutions) in an on-premise environment.

---

## Features

- OCR on PDF, JPEG, or PNG invoices (French language supported)
- Automatic extraction of key invoice fields:
  - Invoice number
  - Invoice date
  - Total amount (TTC)
  - Amount excluding tax (HT)
  - VAT
  - Supplier name
  - Supplier SIRET
  - Supplier address
- REST API for easy integration with other systems
- On-premise deployment (no external API or cloud dependency)

---

## Requirements

- Python 3.9+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (Windows: install and add to PATH)
- [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) (for PDF support, add `bin` to PATH)
- pip packages (see `requirements.txt`):
  - fastapi
  - uvicorn
  - pillow
  - pytesseract
  - pdf2image
  - python-multipart

---

## Installation

1. **Clone the repository**  
   `git clone <repo-url>`

2. **Create and activate a virtual environment**  

    python -m venv venv venv\Scripts\activate

3. **Install dependencies**  

    pip install -r requirements.txt


4. **Install Tesseract OCR**  
   - Download and install from [here](https://github.com/tesseract-ocr/tesseract/wiki#windows).
   - Add the install path (e.g., `C:\Program Files\Tesseract-OCR`) to your system PATH.
   - Ensure the French language pack (`fra.traineddata`) is present in the `tessdata` folder.

5. **Install Poppler for Windows**  
   - Download and extract [Poppler](http://blog.alivate.com.au/poppler-windows/).
   - Add the `bin` directory to your system PATH.

---

## Usage

### Start the API server

    uvicorn main:app --host 0.0.0.0 --port 8000


### API Documentation

Once the server is running, access the interactive documentation at:  
[http://localhost:8000/docs](http://localhost:8000/docs)

### Example Request (using Swagger UI)

- Go to `/docs`
- Use the `/ocr/invoice` endpoint
- Upload a PDF or image of an invoice
- Click "Execute" to see the extracted data

### Example Request (using cURL)

    curl -X POST "http://localhost:8000/ocr/invoice" ^ -H "accept: application/json" ^ -F "file=@C:\path\to\your\invoice.pdf"


---

## API Endpoint

### `POST /ocr/invoice`

- **Description:** Perform OCR and extract invoice data from a PDF or image.
- **Request:** `multipart/form-data` with a single file field named `file`.
- **Response:** JSON object with extracted fields.

#### Example Response

    { "invoice_number": "FAC-2025-00123", "invoice_date": "2025-10-03", "total_amount": 1200.00, "amount_ht": 1000.00, "tva": 200.00, "supplier_name": "Société ABC", "supplier_siret": "12345678900012", "supplier_address": "10 rue de Paris, Lyon" }


---

## Integration with .NET Framework 4.8

- Use `HttpClient` to send HTTP POST requests to the API.
- Send the invoice file as `multipart/form-data`.
- Parse the JSON response to retrieve extracted fields.

---

## Security

- The API is intended for internal (on-premise) use only.
- Restrict network access to trusted clients.
- For production, consider adding authentication (API key, token, etc.).

---

## Troubleshooting

- Ensure Tesseract and Poppler are correctly installed and available in your PATH.
- Check that the French language pack is present for Tesseract.
- Review server logs for error messages.

---

## License

This project is for internal enterprise use. Contact your IT department for licensing and usage policies.

---