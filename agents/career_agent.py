class CareerAgent:

    def __init__(self, client):
        self.client = client

    def career_advice(self, resume_text):

        prompt = f"""
Give career advice based on this resume.

Resume:
{resume_text}

Suggest:

1. Skills to Learn

2. Certifications

3. Projects

4. Career Roadmap
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