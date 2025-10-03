from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from extraction import extract_invoice_data
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import io
import os

# S'assurer que Tesseract est bien trouvé
pytesseract.pytesseract.tesseract_cmd = r"D:\installation\Tesseract-OCR\tesseract.exe"

app = FastAPI()

@app.post("/ocr/invoice")
async def ocr_invoice(file: UploadFile = File(...)):
    content = await file.read()
    images = []

    # Conversion PDF -> images
    if file.filename.lower().endswith(".pdf"):
        images = convert_from_bytes(content)
    else:
        images = [Image.open(io.BytesIO(content))]

    # OCR sur toutes les pages
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img, lang="fra") + "\n"

    # Extraction des champs
    data = extract_invoice_data(text)
    return JSONResponse(content=data)