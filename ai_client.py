import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class CustomOpenAIClient():
    def __init__(self):

        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.github.ai/inference"
        model = "openai/gpt-4.1-nano"

        self.client = OpenAI(base_url=endpoint, api_key=token)
        self.model = model

        self.messages = [
            {
                "role": "user",
                "content": "What is the capital of France?",
            }
        ]

    def send_message(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            messages=self.messages,
            model=self.model
            max_tokens=150,
            n=1,
            stop=None,
            temperature=1.0,
            top_p=1.0
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply