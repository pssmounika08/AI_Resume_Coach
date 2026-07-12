import streamlit as st

from utils.gemini_config import get_gemini_model
from utils.pdf_reader import extract_text_from_pdf
from utils.helper import clean_text

from agents.resume_agent import ResumeAgent
from agents.ats_agent import ATSAgent
from agents.jd_match_agent import JDMatchAgent
from agents.interview_agent import InterviewAgent
from agents.career_agent import CareerAgent

from utils.report_generator import generate_pdf_report


# -----------------------------
# Streamlit Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Resume & Interview Coach",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Load Gemini Model
# -----------------------------

model = get_gemini_model()

# -----------------------------
# Initialize AI Agents
# -----------------------------

resume_agent = ResumeAgent(model)

ats_agent = ATSAgent()

jd_agent = JDMatchAgent(model)

interview_agent = InterviewAgent(model)

career_agent = CareerAgent(model)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🤖 AI Resume Coach")

st.sidebar.markdown("---")

st.sidebar.write("### Features")

st.sidebar.success("✔ Resume Analysis")

st.sidebar.success("✔ ATS Score")

st.sidebar.success("✔ Job Description Matching")

st.sidebar.success("✔ Interview Questions")

st.sidebar.success("✔ Career Suggestions")

st.sidebar.success("✔ PDF Report")

st.sidebar.markdown("---")

st.sidebar.info("Agentic AI Internship Project")

# -----------------------------
# Main Heading
# -----------------------------

st.title("🤖 AI Resume & Interview Coach")

st.write(
    """
Upload your resume and paste a Job Description.

Our AI agents will analyze your resume,
calculate an ATS score,
compare it with the job description,
generate interview questions,
and provide career suggestions.
"""
)

st.divider()

# -----------------------------
# Upload Resume
# -----------------------------

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -----------------------------
# Job Description
# -----------------------------

job_description = st.text_area(
    "Paste Job Description",
    height=220
)

analyze_button = st.button("🚀 Analyze Resume")

# =====================================================
# Resume Analysis
# =====================================================

if analyze_button:

    if uploaded_resume is None:
        st.warning("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.warning("Please paste a Job Description.")
        st.stop()

    with st.spinner("Reading Resume..."):

        resume_text = extract_text_from_pdf(uploaded_resume)

        resume_text = clean_text(resume_text)

    st.success("Resume uploaded successfully!")

    # ------------------------------------
    # Resume Analysis
    # ------------------------------------

    with st.spinner("Analyzing Resume..."):

        resume_analysis = resume_agent.analyze_resume(
            resume_text
        )

    # ------------------------------------
    # ATS Analysis
    # ------------------------------------

    ats_result = ats_agent.calculate_score(
        resume_text,
        job_description
    )

    # ------------------------------------
    # Job Description Match
    # ------------------------------------

    with st.spinner("Comparing Resume with Job Description..."):

        jd_match = jd_agent.match_resume(
            resume_text,
            job_description
        )

    # ------------------------------------
    # Interview Questions
    # ------------------------------------

    with st.spinner("Generating Interview Questions..."):

        interview_questions = interview_agent.generate_questions(
            resume_text,
            job_description
        )

    # ------------------------------------
    # Career Advice
    # ------------------------------------

    with st.spinner("Generating Career Advice..."):

        career_advice = career_agent.career_advice(
            resume_text
        )

    st.divider()

    st.header("📊 ATS Score")

    st.progress(ats_result["score"] / 100)

    st.metric(
        "ATS Match",
        f'{ats_result["score"]}%'
    )

    st.divider()

    st.header("📄 Resume Analysis")

    st.write(resume_analysis)

    st.divider()

    st.header("💼 Job Description Match")

    st.write(jd_match)

    st.divider()

    st.header("🎯 Interview Questions")

    st.write(interview_questions)

    st.divider()

    st.header("🚀 Career Suggestions")

    st.write(career_advice)

    # ------------------------------------
    # Generate PDF Report
    # ------------------------------------

    report_path = "reports/Resume_Report.pdf"

    generate_pdf_report(
        report_path,
        resume_analysis,
        ats_result,
        jd_match,
        interview_questions,
        career_advice
    )

    st.divider()

    st.success("✅ PDF Report Generated Successfully!")

    with open(report_path, "rb") as pdf_file:

        st.download_button(
            label="📥 Download Report",
            data=pdf_file,
            file_name="AI_Resume_Report.pdf",
            mime="application/pdf"
        )