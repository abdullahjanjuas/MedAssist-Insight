# Import Required Libraries
from pdf2image import convert_from_path
import pytesseract
import shutil

# Configure Tesseract path
tesseract_path = shutil.which("tesseract")
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path


def extract_text_with_ocr(pdf_path: str) -> str:
    """
    Converts PDF pages to images and uses OCR to extract all text.
    """
    text = ""
    # Convert PDF pages to images
    pages = convert_from_path(pdf_path)
    
    for i, page in enumerate(pages):
        # OCR the image
        page_text = pytesseract.image_to_string(page)
        text += page_text + "\n"
    
    return text

# Usage
pdf_file = "C:/Users/hp/Desktop/GenAI Medical Assistant/PDF_Processing/Dataset/CMH_Scanned_Report.pdf"
ocr_text = extract_text_with_ocr(pdf_file)
print("Extracted OCR Text:")
print(ocr_text)

# Creating .txt file for raw text
# save_raw_text.py
with open("raw_text.txt", "w", encoding="utf-8") as f:
    f.write(ocr_text)
