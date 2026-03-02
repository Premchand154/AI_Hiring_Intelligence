# AI_Hiring_Intelligence
AI Hiring Intelligence System is an end-to-end resume evaluation platform that combines rule-based scoring, NLP-driven skill extraction, and LLM-generated recruiter summaries. Built with FastAPI and Streamlit, the system analyzes candidate skills, experience, and job fit while incorporating evaluation metrics and fairness simulations.

## Features

✔ Resume skill extraction  
✔ Experience parsing  
✔ Weighted skill scoring  
✔ Experience scoring  
✔ Final composite score  
✔ Candidate categorization  
✔ Recruiter-style LLM summary  
✔ Bias & fairness evaluation simulation  

## Tech Stack

- Python
- FastAPI
- Streamlit
- spaCy
- OpenAI API
- Scikit-learn
- Docker
  
---

## Project Structure

```

AI_Hiring_Intelligence/
│
├── main.py               # FastAPI backend API
├── streamlit_app.py      # Streamlit frontend UI
├── Extract.py            # Resume parsing & skill extraction
├── scoring.py            # Score computation logic
├── llm_summary.py        # LLM-based recruiter summary
├── evaluation.py         # Model evaluation & fairness metrics
├── requirements.txt
├── Dockerfile
└── README.md

````

---

## How It Works

### Resume Parsing
Implemented in `Extract.py`

- Extracts:
  - Skills
  - Years of experience
  - Education
- Computes skill match score
- Generates structured feedback

See: Extract.py

---

### Scoring Logic
- Skill Score (Required + Preferred weighting)
- Experience Score
- Semantic similarity (if used)
- Final Score calculation

Used in: main.py

---

### LLM Summary
If `OPENAI_API_KEY` is set:
- Uses GPT model to generate recruiter-style summary

Otherwise:
- Falls back to structured summary

See: llm_summary.py

---

### API Endpoint

**POST /analyze**

Request Body:

```json
{
  "resume_text": "string",
  "required_skills": ["python", "sql"],
  "preferred_skills": ["aws"],
  "required_experience": 3
}
````

Response:

```json
{
  "parsed_resume": {},
  "scores": {},
  "feedback": {},
  "llm_summary": "string"
}
```

---

## Running Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### Run Frontend (Streamlit)

```bash
streamlit run streamlit_app.py
```

---

## Run With Docker

```bash
docker build -t ai-hiring .
docker run -p 8000:8000 ai-hiring
```

---

## Evaluation & Fairness Metrics

`evaluation.py` includes:

* Accuracy
* Precision
* Recall
* F1-score
* Precision@K
* Group fairness analysis
  * Selection rate
  * Average score comparison

---

## Environment Variables

To enable LLM summary:

```bash
export OPENAI_API_KEY=your_api_key_here
```

---

## Candidate Categorization

| Score Range | Category    |
| ----------- | ----------- |
| ≥ 0.8       | Strong Hire |
| ≥ 0.6       | Consider    |
| ≥ 0.4       | Weak Match  |
| < 0.4       | Reject      |

---

## Future Improvements

* Real embedding-based semantic similarity
* PDF resume parsing
* Database integration
* Admin dashboard
* Bias mitigation layer
* CI/CD pipeline

---







