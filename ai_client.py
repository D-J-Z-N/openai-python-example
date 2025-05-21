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
                "role": "system",
                "content": "You are a helpful assistant. Only respond in Lithuanian",
            }
        ]

    def send_message(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            messages=self.messages,
            model=self.model,
            max_tokens=150,
            temperature=0.7,
            top_p=1.0
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply
