import ollama

def analyze_resume(resume_text: str) -> dict:
    """
    Uses Ollama's local LLM to analyze a resume and provide feedback on strengths, weaknesses, and ATS compatibility.
    """
    prompt = f"""
    You are an AI-powered resume reviewer. Analyze the following resume and provide (in order and numbered) based on the content: {resume_text}

    Note specific feedback and NO MORE THAN 100 WORDS MOST IMPORTANT PART IS #4!


    Response Format:
    1. Strengths (e.g., well-structured, strong keywords, clear experience) with appropriate bolding and italicization.
    2. Weaknesses (e.g., missing sections, weak action verbs, poor formatting) with appropriate bolding and italicization.
    3. Suggestions for improvement with appropriate bolding and italicization.
    4. ATS score (0-100%) based on keyword optimization with appropriate bolding of the percentage other places and italicization.
    
    Return your answer in HTML format (no need for headers, body tags, footers, annotations, titles, or fancy styling other than italicizing and bolding when needed, be sure to bold the score and provide a brief explanation for it at the very end as a percentage.

    """

    response = ollama.chat(model="phi3", messages=[{"role": "user", "content": prompt}])
    print(response)
    feedback = response["message"]["content"]
    return {"feedback": feedback}
