import re


skills_db = [
	"python",
	"pytorch",
	"tensorflow",
	"sql",
    "llm"
	"aws",
	"nlp",
	"machine learning",
	"deep learning",
	"docker",
	"kubernetes",
]

skill_synonyms = {
	"aws": ["amazon web services"],
	"machine learning": ["ml"],
	"deep learning": ["dl"],
}

education_keywords = [
	"bachelor",
	"master",
	"phd",
	"mba",
	"b.sc",
	"m.sc",
	"btech",
	"mtech",
]


def extract_skills(text):
	text_lower = (text or "").lower()
	found = []

	for skill in skills_db:
		pattern = r"\b" + re.escape(skill) + r"\b"
		if re.search(pattern, text_lower):
			found.append(skill)

	for skill, synonyms in skill_synonyms.items():
		for synonym in synonyms:
			pattern = r"\b" + re.escape(synonym) + r"\b"
			if re.search(pattern, text_lower):
				found.append(skill)

	return list(set(found))


def experience_years(text):
	matches = re.search(r"(\d+)\+?\s+years?", (text or "").lower())
	if matches:
		return int(matches.group(1))
	return 0


def education(text):
	text_lower = (text or "").lower()
	for word in education_keywords:
		if word in text_lower:
			return word
	return "Not Found"


def parse_resume(text):
	return {
		"skills": extract_skills(text),
		"experience_years": experience_years(text),
		"education": education(text),
	}


def compute_weighted_skill_match(resume_skills, required_skills, preferred_skills):
	if not required_skills:
		required_match = 0
	else:
		required_match = len(set(resume_skills) & set(required_skills)) / len(required_skills)

	if preferred_skills:
		preferred_match = len(set(resume_skills) & set(preferred_skills)) / len(preferred_skills)
	else:
		preferred_match = 0

	final_score = 0.7 * required_match + 0.3 * preferred_match
	return round(final_score, 2)


def compute_experience_score(resume_years, required_years):
	resume_years = resume_years or 0
	required_years = required_years or 0

	if required_years == 0:
		return 1.0

	experience_score = min(resume_years / required_years, 1.0)
	return round(experience_score, 2)


def compute_final_score(skill_score, experience_score, semantic_similarity_score):
	final_score = 0.5 * skill_score + 0.3 * experience_score + 0.2 * semantic_similarity_score
	return round(final_score, 2)


def generate_feedback(
	resume_skills,
	required_skills,
	preferred_skills,
	resume_experience,
	required_experience,
):
	feedback = {}
	matched_required = list(set(resume_skills) & set(required_skills))
	missing_required = list(set(required_skills) - set(resume_skills))
	matched_preferred = list(set(resume_skills) & set(preferred_skills))

	resume_experience = resume_experience or 0
	required_experience = required_experience or 0
	experience_gap = required_experience - resume_experience

	strengths = []
	for skill in matched_required:
		strengths.append(f"Matches required skill: {skill}")
	for skill in matched_preferred:
		strengths.append(f"Has preferred skill: {skill}")

	gaps = []
	for skill in missing_required:
		gaps.append(f"Missing required skill: {skill}")
	if experience_gap > 0:
		gaps.append(f"Experience gap: {experience_gap} years less than required")

	recommendations = []
	for skill in missing_required:
		recommendations.append(f"Consider learning: {skill}")
	if experience_gap > 0:
		recommendations.append("Gain more experience in the field to meet the requirement")

	feedback["strengths"] = strengths
	feedback["gaps"] = gaps
	feedback["recommendations"] = recommendations
	return feedback


def categorize_candidate(final_score):
	if final_score >= 0.8:
		return "Strong Hire"
	if final_score >= 0.6:
		return "consider"
	if final_score >= 0.4:
		return "Weak Match"
	return "Reject"
