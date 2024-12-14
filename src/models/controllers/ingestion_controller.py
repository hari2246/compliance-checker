import PyPDF2
from flask import jsonify

def extract_text_from_pdf(filepath):
    try:
        with open(filepath, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            if not text.strip():
                return jsonify({"error": "No text found in the PDF"}), 400
            return text
    except Exception as e:
        return jsonify({"error": f"Failed to extract text: {str(e)}"}), 500
