from openai import OpenAI


# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

chat_response = client.chat.completions.create(
    model="OpenLemur/lemur-70b-chat-v1",  # or try smaller, "facebook/opt-125m".
    messages=[
        {"role": "system", "content": "You are a helpful, respectful, and honest assistant."},
        {"role": "user", "content": "Write a Python function to merge two sorted lists into one sorted list without using any built-in sort functions."},
    ],
)
print("Chat response:", chat_response)
