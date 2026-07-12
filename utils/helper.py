import re


def clean_text(text):
    """
    Clean extracted PDF text by removing extra spaces and blank lines.
    """
    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text


def calculate_resume_length(text):
    """
    Returns the number of words in the resume.
    """
    if not text:
        return 0

    return len(text.split())


def format_score(score):
    """
    Ensures score is between 0 and 100.
    """
    try:
        score = int(score)
    except:
        score = 0

    score = max(0, min(score, 100))

    return score


def extract_skills(text):
    """
    Very simple skill extractor.
    """

    skills_database = [
        "python",
        "java",
        "c++",
        "c",
        "sql",
        "mysql",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "excel",
        "power bi",
        "aws",
        "docker",
        "git",
        "github",
        "linux",
        "streamlit",
        "pandas",
        "numpy",
        "flask",
        "fastapi"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(found_skills)