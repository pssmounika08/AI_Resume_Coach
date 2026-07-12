class InterviewAgent:

    def __init__(self, client):
        self.client = client

    def generate_questions(self, resume_text, job_description):

        prompt = f"""
Generate interview questions.

Resume:
{resume_text}

Job Description:
{job_description}

Generate:

5 Technical Questions

3 HR Questions

2 Behavioral Questions
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