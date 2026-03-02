def compute_scores(parsed_resume,
                   required_skills,
                   preferred_skills,
                   required_exp):

    resume_skills = parsed_resume.get("skills", [])
    resume_exp = parsed_resume.get("experience_years")

    # ---- SAFETY FIXES ----
    if resume_exp is None:
        resume_exp = 0

    if required_exp is None or required_exp == 0:
        exp_score = 1.0  # If no experience required, full score
    else:
        exp_score = min(resume_exp / required_exp, 1.0)

    # Prevent division by zero
    if not required_skills:
        required_match = 1.0
    else:
        required_match = len(set(resume_skills) & set(required_skills)) / len(required_skills)

    preferred_match = 0
    if preferred_skills:
        preferred_match = len(set(resume_skills) & set(preferred_skills)) / len(preferred_skills)

    skill_score = 0.7 * required_match + 0.3 * preferred_match

    final_score = 0.5 * skill_score + 0.3 * exp_score + 0.2 * 0.5  # placeholder semantic score

    return {
        "skill_score": round(skill_score, 2),
        "experience_score": round(exp_score, 2),
        "final_score": round(final_score, 2)
    }