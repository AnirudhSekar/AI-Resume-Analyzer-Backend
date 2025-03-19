import fitz  # PyMuPDF

def extract_resume_text(file_content: bytes) -> str:
    """
    Extracts text from a resume PDF.
    """
    doc = fitz.open(stream=file_content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    
    return text.strip()  # Remove extra spaces
