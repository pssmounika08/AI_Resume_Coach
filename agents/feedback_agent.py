class FeedbackAgent:
    """
    AI Agent that evaluates interview answers.
    """

    def __init__(self, model):
        self.model = model

    def evaluate_answer(self, question, answer):

        prompt = f"""
You are an interview evaluator.

Question:

{question}

Candidate Answer:

{answer}

Evaluate using:

1. Score (Out of 10)

2. Strengths

3. Weaknesses

4. Suggestions for Improvement
"""

        response = self.model.generate_content(prompt)

        return response.text