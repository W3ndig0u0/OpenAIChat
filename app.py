import os
import openai


print("HUH?!")

openai.api_key = os.getenv(
    "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")
response = openai.Completion.create(
    model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
