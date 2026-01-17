import pdfplumber
import camelot
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"

    return full_text


def extract_tables_from_pdf(pdf_path: str):
    tables = camelot.read_pdf(pdf_path, pages="all")
    return [table.df for table in tables]


pdf_file = r"C:/Users/hp/Desktop/GenAI Medical Assistant/PDF Processing/Dataset/Tabular_Sample.pdf"

# ---- TEXT EXTRACTION ----
text = extract_text_from_pdf(pdf_file)

output_dir = r"C:/Users/hp/Desktop/GenAI Medical Assistant/PDF Processing/Output"
os.makedirs(output_dir, exist_ok=True)

raw_text_path = os.path.join(output_dir, "raw_text.txt")

with open(raw_text_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"raw_text.txt saved at:\n{raw_text_path}")

# ---- TABLE EXTRACTION (OPTIONAL) ----
try:
    tables = extract_tables_from_pdf(pdf_file)
    for i, table in enumerate(tables):
        print(f"\nTable {i + 1}:")
        print(table)
except Exception as e:
    print("No Tables Found in your uploaded file! Please try using pdf extractor.", e)
