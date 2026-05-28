import streamlit as st
import pdfplumber
import nltk
import string
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide"
)

nltk.download("stopwords")


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()

skills_list = [
    "python", "sql", "machine learning", "data analysis", "java", "c++",
    "html", "css", "javascript", "streamlit", "nlp", "ai", "flask",
    "fastapi", "git", "github", "excel", "power bi", "pandas", "numpy", "apis"
]

required_skills = [
    "python", "sql", "data analysis", "apis", "git", "github",
    "machine learning", "nlp", "streamlit", "pandas", "numpy"
]


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    stop_words = set(stopwords.words("english"))
    words = text.split()

    cleaned_words = [word for word in words if word not in stop_words]
    return " ".join(cleaned_words)


def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def find_missing_skills(found_skills):
    missing_skills = []

    for skill in required_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills


def get_recommendation(match_score):
    if match_score >= 75:
        return "Shortlist"
    elif match_score >= 50:
        return "Consider"
    else:
        return "Reject"


st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}
.subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}
.section-card {
    padding: 20px;
    border-radius: 14px;
    background-color: #f8f9fb;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}
.metric-card {
    padding: 18px;
    border-radius: 14px;
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Resume Screening System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Rank resumes against a job description using semantic similarity and skill matching.</div>',
    unsafe_allow_html=True
)

left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("### Upload Resumes")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF resumes",
        type="pdf",
        accept_multiple_files=True
    )

with right_col:
    st.markdown("### Job Description")
    job_description = st.text_area(
        "Paste the job description here",
        height=180,
        placeholder="Example: Looking for a Python developer with SQL, ML, APIs, and data analysis skills..."
    )

st.divider()

if uploaded_files and job_description:
    results = []

    with st.spinner("Analyzing resumes..."):
        for uploaded_file in uploaded_files:
            with pdfplumber.open(uploaded_file) as pdf:
                text = ""

                for page in pdf.pages:
                    extracted_text = page.extract_text()

                    if extracted_text:
                        text += extracted_text + " "

            cleaned_text = clean_text(text)
            found_skills = extract_skills(cleaned_text)
            missing_skills = find_missing_skills(found_skills)

            resume_embedding = model.encode([cleaned_text])
            job_embedding = model.encode([job_description])

            similarity_score = cosine_similarity(resume_embedding, job_embedding)[0][0]
            match_percentage = round(float(similarity_score) * 100, 2)
            recommendation = get_recommendation(match_percentage)

            results.append({
                "Resume Name": uploaded_file.name,
                "Match Score": match_percentage,
                "Skills Found": ", ".join(found_skills) if found_skills else "None",
                "Missing Skills": ", ".join(missing_skills) if missing_skills else "None",
                "Recommendation": recommendation
            })

    results = sorted(
        results,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    df = pd.DataFrame(results)
    df.index = df.index + 1

    top_candidate = results[0]
    shortlisted = len([r for r in results if r["Recommendation"] == "Shortlist"])
    considered = len([r for r in results if r["Recommendation"] == "Consider"])
    rejected = len([r for r in results if r["Recommendation"] == "Reject"])

    st.markdown("## Screening Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Resumes", len(results))
    col2.metric("Shortlisted", shortlisted)
    col3.metric("Consider", considered)
    col4.metric("Rejected", rejected)

    st.success(
        f"Best match: {top_candidate['Resume Name']} "
        f"with {top_candidate['Match Score']}% match"
    )

    st.markdown("## Candidate Ranking")
    st.dataframe(df, use_container_width=True)

elif uploaded_files and not job_description:
    st.info("Paste a job description to start screening resumes.")

elif job_description and not uploaded_files:
    st.info("Upload at least one resume to start screening.")

else:
    st.info("Upload resumes and paste a job description to begin.")