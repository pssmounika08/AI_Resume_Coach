class JDMatchAgent:

    def __init__(self, client):
        self.client = client

    def match_resume(self, resume_text, job_description):

        prompt = f"""
Compare this resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:

1. Match Percentage

2. Matching Skills

3. Missing Skills

4. Final Recommendation
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