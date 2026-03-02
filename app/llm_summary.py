import os
from openai import OpenAI


def _fallback_summary(scores, feedback):
    strengths = feedback.get("strengths", [])
    gaps = feedback.get("gaps", [])
    recommendations = feedback.get("recommendations", [])

    parts = [
        f"Final score: {scores.get('final_score', 0)}.",
        f"Skill score: {scores.get('skill_score', 0)}.",
        f"Experience score: {scores.get('experience_score', 0)}.",
    ]

    if strengths:
        parts.append("Strengths: " + "; ".join(strengths) + ".")
    if gaps:
        parts.append("Gaps: " + "; ".join(gaps) + ".")
    if recommendations:
        parts.append("Recommendations: " + "; ".join(recommendations) + ".")

    return " ".join(parts)


def generate_llm_summary(scores, feedback):
    prompt = f"""
    You are an AI hiring assistant.

    Candidate Evaluation Data:
    Final Score: {scores['final_score']}
    Skill Score: {scores['skill_score']}
    Experience Score: {scores['experience_score']}

    Strengths:
    {feedback['strengths']}

    Gaps:
    {feedback['gaps']}

    Generate a professional recruiter-style evaluation summary.
    Do not add any new information.
    """

    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return _fallback_summary(scores, feedback)

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content or _fallback_summary(scores, feedback)
    except Exception:
        return _fallback_summary(scores, feedback)
