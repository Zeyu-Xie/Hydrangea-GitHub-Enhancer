import requests
import json


def query_ollama(model_name, prompt):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are a professional specialist in the field of systems and computer sciences. Every time you answer a question, you speak the answer directly."},
            {"role": "user", "content": prompt},
        ],
        "stream": True,
    }

    response = requests.post(url, json=payload, headers=headers, stream=True)
    if response.status_code != 200:
        raise Exception(
            f"HTTP Error: {response.status_code}, Content: {response.text}")

    full_response = ""
    try:
        for line in response.iter_lines(decode_unicode=True):
            if line.strip():
                data = json.loads(line)
                if "message" in data and "content" in data["message"]:
                    full_response += data["message"]["content"]
    except json.JSONDecodeError as e:
        print("JSON Parse Error:", e)
        print("Error located at row:", line)

    return full_response


model_name = "llama3.2"
prompt = "What's the capital of France? Only tell me the answer."
response = query_ollama(model_name, prompt)
print(response)
