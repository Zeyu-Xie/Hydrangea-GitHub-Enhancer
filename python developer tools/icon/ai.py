import requests
import json
import os


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


def type_list():
    path = os.path.join(os.path.dirname(__file__), "type_list.txt")
    with open(path, "r") as file:
        return file.read().splitlines()

def csv_list():
    path = os.path.join(os.path.dirname(__file__), "icon_description.csv")
    with open(path, "r") as file:
        return file.read().splitlines()

if __name__ == "__main__":

    tp_list = type_list()
    c_list = csv_list()[1:]
    l = len(tp_list)

    pt = os.path.join(os.path.dirname(__file__), "newresult.csv")
    with open(pt, "w") as file:
        file.write("ext.,description,used by\n")

    for i in range(l):

        tp = tp_list[i]
        c = c_list[i]
        model_name = "llama3.2"
        prompt = f"Tell me the description of the extension \"{tp}\" according to the hint \"{c}\", no more than 5 words."
        r1 = query_ollama(model_name, prompt)

        prompt = f"Tell me the software or situation to use the extension \"{tp}\" according to the hint \"{c}\", no more than 5 words."
        r2 = query_ollama(model_name, prompt)

        print(f"\"{tp}\", \"{r1}\", \"{r2}\"")
        with open(pt, "a") as file:
            file.write(f"\"{tp}\", \"{r1}\", \"{r2}\"\n")