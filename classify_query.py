from dotenv import load_dotenv
import os
from together import Together

load_dotenv()
together_api_key = os.getenv("TOGETHER_API_KEY")

client = Together()
headers = {
    "Authorization": f"Bearer {together_api_key}"
}

def related(query):
    stream = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{
            "role": "user",
            "content": (
                "Classify if the given query is specifically asking for the current price of bitcoin, ethereum, or any other cryptocurrency. "
                "Respond with:\nYES\n<cryptocurrency_name>\nif the query is about the price, or\nNO\nif it is not asking about the price.\n"
                "Example queries and responses:\n"
                " - 'What is the price of bitcoin?' should return 'YES\nBitcoin'.\n"
                " - 'Tell me about bitcoin' should return 'NO'.\n"
                " - 'Current value of Ethereum?' should return 'YES\nEthereum'.\n"
                "This is the query: " + query

            )
        }],
        stream=True,
    )

    response_text = ""
    for chunk in stream:
        response_text += chunk.choices[0].delta.content or ""

    response_lines = response_text.splitlines()
    flag = response_lines[0].strip()
    crypto = response_lines[1].strip() if flag == "YES" and len(response_lines) > 1 else None
    return flag, crypto
