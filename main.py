from fastapi import FastAPI
from Extract import parse_resume, generate_feedback
from scoring import compute_scores
from pydantic import BaseModel
from llm_summary import generate_llm_summary
from typing import List

app = FastAPI(title="AI Hiring Intelligence API")

class AnalyzeRequest(BaseModel):
    resume_text: str
    required_skills: List[str]
    preferred_skills: List[str]
    required_experience: int
@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    parsed = parse_resume(request.resume_text)
    required_skills = request.required_skills
    preferred_skills = request.preferred_skills
    required_experience = request.required_experience

    scores = compute_scores(
        parsed,
        required_skills,
        preferred_skills,
        required_experience
    )

    feedback = generate_feedback(
        parsed["skills"],
        required_skills,
        preferred_skills,
        parsed["experience_years"],
        required_experience
    )
    llm_summary = generate_llm_summary(scores, feedback)
    return {
        "parsed_resume": parsed,
        "scores": scores,
        "feedback": feedback,
        "llm_summary": llm_summary
    }