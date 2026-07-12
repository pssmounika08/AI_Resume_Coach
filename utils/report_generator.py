from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    filename,
    resume_analysis,
    ats_result,
    jd_match,
    interview_questions,
    career_advice
):
    """
    Generate a PDF report containing all AI analysis.
    """

    document = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "AI Resume & Interview Coach Report",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))

    sections = [
        ("Resume Analysis", resume_analysis),
        ("ATS Analysis", str(ats_result)),
        ("Job Description Match", jd_match),
        ("Interview Questions", interview_questions),
        ("Career Advice", career_advice)
    ]

    for heading, content in sections:

        story.append(
            Paragraph(f"<b>{heading}</b>", styles["Heading2"])
        )

        story.append(
            Paragraph(str(content).replace("\n", "<br/>"),
            styles["BodyText"])
        )

        story.append(Spacer(1, 15))

    document.build(story)

    return filename