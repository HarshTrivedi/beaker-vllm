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
        {"role": "system", "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request."},
        {"role": "user", "content": "Write a Python function to merge two sorted lists into one sorted list without using any built-in sort functions."},
    ],
    temperature=0.0,
    max_tokens=300,
)
print(chat_response.choices[0].message.content)
