class ATSAgent:
    """
    Simulates an ATS (Applicant Tracking System)
    by comparing resume content with a job description.
    """

    def calculate_score(self, resume_text, job_description):

        resume_words = set(resume_text.lower().split())
        jd_words = set(job_description.lower().split())

        common_words = resume_words.intersection(jd_words)

        if len(jd_words) == 0:
            return {
                "score": 0,
                "matched_keywords": [],
                "missing_keywords": []
            }

        score = int((len(common_words) / len(jd_words)) * 100)

        matched = sorted(list(common_words))

        missing = sorted(list(jd_words - resume_words))

        return {
            "score": min(score, 100),
            "matched_keywords": matched[:20],
            "missing_keywords": missing[:20]
        }