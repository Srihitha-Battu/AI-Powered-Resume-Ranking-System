import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Function to extract and clean text from PDF
def extract_text_from_pdf(file):
    try:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from each page
        return text
    except Exception as e:
        st.error(f"Error extracting text from {file.name}: {str(e)}")
        return ""

# Text Preprocessing Function
def preprocess_text(text):
    # Remove extra spaces, newlines, and special characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespaces/newlines with a single space
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)  # Remove special characters (keep only alphanumeric and spaces)
    text = text.lower()  # Convert text to lowercase
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    # Combine job description with resumes
    documents = [job_description] + resumes  # Add job description to the list of resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)  # Vectorize all documents
    vectors = vectorizer.toarray()  # Get the vector representation of documents

    # Calculate cosine similarity
    job_description_vector = vectors[0]  # The first vector is the job description
    resume_vectors = vectors[1:]  # The rest are resume vectors
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()  # Calculate similarity
    
    return cosine_similarities

# Streamlit app
st.title("AI Resume Screening & Candidate Ranking System")

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter the job description")

# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)  # Extract text from each uploaded PDF
        if text:
            cleaned_text = preprocess_text(text)  # Preprocess the extracted text
            resumes.append(cleaned_text)

    if len(resumes) > 0:
        # Rank resumes based on cosine similarity
        scores = rank_resumes(job_description, resumes)

        # Display the results in a DataFrame
        results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
        results = results.sort_values(by="Score", ascending=False)  # Sort the resumes by score (highest first)

        # Display the ranking
        st.write(results)

        # Visualization: Bar chart for resume scores
        st.header("Resume Score Visualization")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Score', y='Resume', data=results, palette='viridis')
        plt.title("Resume Ranking Based on Job Description")
        plt.xlabel("Cosine Similarity Score")
        plt.ylabel("Resumes")
        st.pyplot(plt)  # Display the plot

    else:
        st.warning("No valid resumes uploaded. Please upload resumes with extractable text.")
