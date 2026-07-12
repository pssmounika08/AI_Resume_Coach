# 🤖 AI Resume & Interview Coach

An AI-powered web application that helps job seekers analyze their resumes, calculate ATS scores, compare resumes with job descriptions, generate interview questions, and receive personalized career suggestions.

Built using **Python**, **Streamlit**, and **OpenRouter AI**.

---

## 🚀 Features

- 📄 Resume Analysis
- 🎯 ATS Score Calculation
- 🔍 Job Description Matching
- 💼 AI-Generated Interview Questions
- 📈 Career Suggestions
- 📥 Upload Resume (PDF)
- ⚡ Fast and Interactive Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenRouter API
- PDFPlumber
- Python-dotenv
- ReportLab
- Pandas

---

## 📂 Project Structure

```
AI_Resume_Coach/
│
├── agents/
│   ├── resume_agent.py
│   ├── ats_agent.py
│   ├── interview_agent.py
│   ├── career_agent.py
│
├── utils/
│   ├── gemini_config.py
│   └── pdf_reader.py
│
├── uploads/
├── reports/
├── assets/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI_Resume_Coach.git

cd AI_Resume_Coach
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📌 How It Works

1. Upload your resume in PDF format.
2. Paste the job description.
3. Click **Analyze Resume**.
4. The application generates:
   - Resume Analysis
   - ATS Score
   - Resume vs Job Description Match
   - Interview Questions
   - Career Suggestions

---

## 📦 Requirements

- Python 3.10+
- Streamlit
- OpenRouter API Key

---

## 🎯 Future Enhancements

- Cover Letter Generator
- Resume Improvement Suggestions
- LinkedIn Profile Optimizer
- Skill Gap Analysis
- Resume Templates
- Download Report as PDF
- Multi-language Support

---

## 👩‍💻 Developer

**P. Sai Sri Mounika**

---

## 📄 License

This project is developed for educational and portfolio purposes.
