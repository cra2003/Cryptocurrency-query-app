from classify_query import related
from translate import translate_text
from cachetools import TTLCache
from redis import Redis
import requests
from dotenv import load_dotenv
import os
from together import Together
from crypto_price import get_crypto_price

# Now you can use get_crypto_price as needed in your main application


load_dotenv()

# Initialize necessary components
together_api_key = os.getenv("TOGETHER_API_KEY")

client = Together()
headers = {
    "Authorization": f"Bearer {together_api_key}"
}
redis = Redis(host='localhost', port=6379, db=0)
cache = TTLCache(maxsize=100, ttl=300)

def manage_context(session_id, query, response_text):
    # Retrieve previous conversation history from Redis
    history = redis.get(session_id)
    if history:
        history = history.decode("utf-8")
    else:
        history = ""

    # Update conversation history with the new query and response
    updated_history = f"{history}\nUser: {query}\nAssistant: {response_text}"
    if len(updated_history) > 8192:  # Respecting MAX_CONTEXT_SIZE of 8192 tokens
        updated_history = updated_history[-8192:]
    redis.set(session_id, updated_history)
    print(updated_history)

def final(session_id, query, source_language="English"):
    # Translate if source language isn't English
    if source_language != "English":
        print("Translating...")
        query = translate_text(source_language, query)
    
    # Fetch conversation history from Redis
    history = redis.get(session_id)
    if history:
        history = history.decode("utf-8")
    else:
        history = ""
    
    # Determine if the query is related to a cryptocurrency
    flag, crypto = related(query)
    print(flag, crypto)

    # Handle cryptocurrency-related queries
    if flag == "YES" and crypto:
        cryptoid = crypto.lower()
        crypt_price = get_crypto_price(cryptoid)
        price_message = f"The price of {crypto} is {crypt_price} USD." if crypt_price else "Price cannot be fetched."

        # Get a response from the Together client with crypto info
        stream = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Here is the conversation history:\n{history}\n"
                        f"Mostly focus on the current query. Only refer to the conversation history if required to maintain context or clarify details.\n"
                        f"Do not deviate from the main topic.\n"
                        f"Answer the query properly using the price message.If it is a comparison between prices , try using history"
                        f"Crypto info: {price_message}\n"
                        f"The user's question is: '{query}'"

                    )
                }
            ],
            stream=True,
        )

        # Construct response from stream
        response_text = ""
        for chunk in stream:
            response_text += chunk.choices[0].delta.content or ""
    else:
        # If not crypto-related, provide a general response
        stream = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[{
                "role": "user",
                "content": (
                    f"Here is the conversation history:\n{history}\n"
                    "Answer the user's query in a general way, without focusing solely on cryptocurrency, unless contextually relevant. "
                    "Use the history to maintain context only if necessary, especially in cases of ambiguous or incomplete queries. "
                    "For example, if a query lacks a specific cryptocurrency name but references a previous question (e.g., 'what is it now'), "
                    "refer back to the last mentioned cryptocurrency and its price to maintain continuity.\n"
                    "Other than that answer the query in the most general way"
                    f"The user's question is: '{query}'"

                )
            }],
            stream=True,
        )

        # Construct response from stream
        response_text = ""
        for chunk in stream:
            response_text += chunk.choices[0].delta.content or ""

    # Update Redis with the new conversation history
    manage_context(session_id, query, response_text)
    return response_text
