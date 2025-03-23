# AI-Powered Resume Ranking System

An AI-powered tool to screen and rank resumes based on job descriptions. This project automates the process of evaluating and ranking resumes using Natural Language Processing (NLP) techniques, such as **TF-IDF vectorization** and **cosine similarity**.

---

## Features
- **Resume Parsing**: Extracts text from uploaded PDF resumes.
- **Text Preprocessing**: Cleans and standardizes text for analysis.
- **Job Description Matching**: Uses TF-IDF and cosine similarity to match resumes with job descriptions.
- **Ranking**: Ranks resumes based on their similarity scores.
- **Visualization**: Displays results in a table and bar chart for easy interpretation.

---

## How It Works
1. **Input**:
   - The user provides a job description and uploads one or more resumes in PDF format.
2. **Text Extraction**:
   - The system extracts text from the uploaded PDF resumes.
3. **Text Preprocessing**:
   - The extracted text is cleaned and standardized (e.g., removing special characters, converting to lowercase).
4. **TF-IDF Vectorization**:
   - The job description and resumes are converted into numerical vectors using TF-IDF.
5. **Cosine Similarity**:
   - The similarity between the job description and each resume is calculated using cosine similarity.
6. **Ranking**:
   - Resumes are ranked based on their similarity scores.
7. **Output**:
   - The results are displayed in a table and visualized using a bar chart.

---

## Installation

### Prerequisites
- Python 3.8+
- Git (optional, for cloning the repository)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Srihitha-Battu/AI-Powered-Resume-Ranking-System.git