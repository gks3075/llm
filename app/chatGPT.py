import requests

url = "https://norchestra.maum.ai/harmonize/dosmart"

headers = {
    "Content-Type": "application/json"
}

data = {
    "app_id": "b075b6a9-f012-5a1e-979e-4b3bf54ce353",
    "name": "demo",
    "item": [
        "chatgpt-text-davinci-003"
    ],
    "param": [
        {
            "text": "안녕"
        }
    ]
}

response = requests.post(url, json=data, headers=headers)
print(response.text)

def chatGPT(text):
    data = {
    "app_id": "b075b6a9-f012-5a1e-979e-4b3bf54ce353",
    "name": "demo",
    "item": [
        "chatgpt-text-davinci-003"
    ],
    "param": [
        {
            "text": f"{text}"
        }
    ]
}
    response = requests.post(url, json=data, headers=headers)
    return response.text