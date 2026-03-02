import streamlit as st
import requests

st.set_page_config(page_title="AI Hiring Intelligence", layout="wide")
st.title("AI Hiring Intelligence System")
st.markdown("Evaluate resumes using structured AI scoring and LLM feedback.")

resume_text=st.text_area("Paste Resume Text Here", height=200)
job_required=st.text_input("Required Skills (comma separated)")
job_preferred=st.text_input("Preferred Skills (comma separated)")
required_exp=st.number_input("Required Experience (years)", min_value=0)

if st.button("Analyze Resume"):
    payload={
        "resume_text": resume_text,
        "required_skills": [s.strip().lower() for s in job_required.split(",") if s],
        "preferred_skills": [s.strip().lower() for s in job_preferred.split(",") if s],
        "required_experience": required_exp
    }
    response=requests.post("http://localhost:8000/analyze", json=payload)
    if response.status_code==200:
        result=response.json()
        st.subheader("Scores")
        st.write(result["scores"])
        
        st.progress(result["scores"]["final_score"])
        if result["scores"]["final_score"]>=0.8:
            st.success("Strong Candidate")
        elif result["scores"]["final_score"]>=0.6:
            st.warning("consider")
        else:
            st.error("Weak Match")    
        
        st.subheader("Strengths")
        for s in result["feedback"]["strengths"]:
            st.success(s)
        
        st.subheader("Gaps")
        for g in result["feedback"]["gaps"]:
            st.warning(g)
        
        st.subheader("LLM Summary")
        st.info(result["llm_summary"])
    else:
        st.error("API Error. Check backend.")            
        