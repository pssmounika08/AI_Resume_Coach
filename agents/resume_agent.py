class ResumeAgent:
    def __init__(self, client):
        self.client = client

    def analyze_resume(self, resume_text):

        prompt = f"""
You are an expert HR recruiter.

Analyze the following resume.

Resume:
{resume_text}

Provide:
1. Professional Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions
6. Resume Score out of 10
"""

        response = self.client.chat.completions.create(
           model="meta-llama/llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content