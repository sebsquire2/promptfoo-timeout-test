from openai import AsyncOpenAI, OpenAI
import requests

async_client = AsyncOpenAI()
client = OpenAI()


def call_api(prompt, options, context):
    # Get config values
    some_option = options.get("config").get("someOption")

    url = "http://127.0.0.1:5000/predict"
    headers = {"Content-Type": "application/json"}
    data = {"inputText": prompt}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed", "status_code": response.status_code, "output": response.text}


def some_other_function(prompt, options, context):
    return call_api(prompt + "\nWrite in ALL CAPS", options, context)


async def async_provider(prompt, options, context):
    chat_completion = await async_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a marketer working for a startup called Bananamax.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model="gpt-4o",
    )

    return {"output": chat_completion.choices[0].message.content}