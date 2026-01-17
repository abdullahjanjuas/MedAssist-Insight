# Required imports
import pdfplumber
import camelot
import os
from pdf2image import convert_from_path
import pytesseract
import shutil

# Configure Tesseract path
tesseract_path = shutil.which("tesseract")
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

# PDF Text Extraction Function
def extract_text_from_pdf(pdf_path: str) -> str:
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"

    return full_text

# PDF Table Extraction Function
def extract_tables_from_pdf(pdf_path: str):
    tables = camelot.read_pdf(pdf_path, pages="all")
    return [table.df for table in tables]

# OCR Text Extraction Function
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


def main():
    # PDF File Path
    pdf_file = r"C:/Users/hp/Desktop/GenAI Medical Assistant/PDF Processing/Dataset/Tabular_Sample.pdf"

    # TEXT EXTRACTION 
    text = extract_text_from_pdf(pdf_file)

    output_dir = r"C:/Users/hp/Desktop/GenAI Medical Assistant/PDF Processing/Output"
    os.makedirs(output_dir, exist_ok=True)

    raw_text_path = os.path.join(output_dir, "raw_text.txt")

    with open(raw_text_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"raw_text.txt saved at:\n{raw_text_path}")

    # TABLE EXTRACTION
    try:
        tables = extract_tables_from_pdf(pdf_file)
        for i, table in enumerate(tables):
            print(f"\nTable {i + 1}:")
            print(table)
    except Exception as e:
        print("No Tables Found in your uploaded file! Please try using pdf extractor.", e)

    # Usage
    image_pdf_file = "C:/Users/hp/Desktop/GenAI Medical Assistant/PDF Processing//Dataset/Image_Report.pdf"
    ocr_text = extract_text_with_ocr(image_pdf_file)
    print("Extracted OCR Text:")
    print(ocr_text)

if __name__ == "__main__":
    main()