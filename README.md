# AI-BASED-RESUME-SCREENING-SYSTEM

End-to-end AI-powered Resume Screening System for ranking resumes against job descriptions using Natural Language Processing (NLP), semantic similarity, skill extraction, and candidate recommendations.

> **Why This Project Matters: The Hiring Problem**
>
> In modern recruitment, recruiters often receive hundreds of resumes for a single role, making manual screening time-consuming and inefficient. Traditional filtering methods rely heavily on keyword matching, which often misses relevant candidates whose skills are expressed differently.
>
> **The Solution**
>
> This project introduces an AI-powered resume screening system that uses semantic similarity and NLP techniques to rank resumes intelligently. Instead of simple keyword matching, the system compares the contextual meaning of resumes with a job description, extracts relevant technical skills, identifies missing competencies, and recommends candidates for shortlisting.

# Tools & Technologies

> **Python** – Core application logic and NLP pipeline.

> **Streamlit** – Interactive web application interface for resume screening and ranking.

> **Sentence Transformers** – Semantic embedding generation for intelligent resume-job matching.

> **Scikit-learn** – Cosine similarity computation for semantic relevance scoring.

> **NLTK (Natural Language Toolkit)** – Resume text preprocessing, stopword removal, and cleaning.

> **PDFPlumber** – PDF parsing and resume text extraction.

> **Pandas** – Data processing and ranking table visualization.

> **VS Code** – Primary development environment.

# Project Workflow / Steps

## 1. Resume Upload & Parsing

> Upload multiple resumes in PDF format using Streamlit.

> Extract textual content from resumes using PDFPlumber.

> Parse multiple resumes simultaneously for batch screening.

## 2. Text Cleaning & NLP Processing

> Convert extracted resume text into normalized lowercase format.

> Remove punctuation and stopwords using NLTK.

> Clean noisy resume data for improved semantic analysis.

## 3. Semantic Resume Matching

> Convert resumes and job descriptions into vector embeddings using Sentence Transformers.

> Compute semantic similarity scores through cosine similarity.

> Rank resumes according to contextual relevance instead of keyword matching.

## 4. Skill Extraction

> Extract relevant technical skills from resumes.

> Match detected skills against required job skills.

> Generate candidate skill summaries automatically.

## 5. Candidate Recommendation Engine

> Classify candidates into:
>
> * Shortlist
> * Consider
> * Reject
>
> based on semantic match score thresholds.

## 6. Resume Ranking Dashboard

> Display ranked candidate information in a structured table.

> Show:
>
> * Resume Name
> * Match Score
> * Skills Found
> * Missing Skills
> * Recommendation

# Features

> Semantic Resume Matching: Intelligent contextual matching using transformer embeddings.

> Multiple Resume Screening: Upload and rank multiple resumes simultaneously.

> Skill Extraction: Detect candidate technical skills automatically.

> Skill Gap Analysis: Identify missing competencies relative to job requirements.

> Candidate Recommendation System: Shortlist, Consider, or Reject candidates automatically.

> Interactive Dashboard: Clean Streamlit interface for screening and ranking resumes.

# Key Results & Insights

> Reduced manual resume filtering by automatically ranking resumes based on semantic relevance.

> Improved candidate evaluation through contextual AI matching instead of exact keyword dependency.

> Automated skill extraction and recommendation generation for faster recruiter decision-making.

> Created a lightweight and deployable AI screening workflow suitable for internship-scale recruitment systems.

# Future Improvements

> Add support for DOCX resumes.

> Integrate LLM-based resume feedback generation.

> Export ranked candidate reports as CSV/PDF.

> Add recruiter authentication and candidate database storage.

> Deploy on cloud infrastructure for real-time hiring workflows.

# Contributing & Licensing

Contributions, issues, and feature requests are welcome.

Distributed under the MIT License.
