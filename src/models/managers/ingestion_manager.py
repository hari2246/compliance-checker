import PyPDF2

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""  # Handle empty pages
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""
    return text
