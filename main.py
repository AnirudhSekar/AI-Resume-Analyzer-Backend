from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_resume_text
from ai_analysis import analyze_resume

app = FastAPI()

# ✅ Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend to access API
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    """
    Receives a resume PDF, extracts text, and analyzes it with Ollama.
    """
    content = await file.read()
    extracted_text = extract_resume_text(content)
    feedback = analyze_resume(extracted_text)

    return {"feedback": feedback}
