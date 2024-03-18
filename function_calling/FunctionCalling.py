import logging
import requests
from openai import OpenAI


api_key=""


# GPT_MODEL_3 = "gpt-3.5-turbo-0125"
GPT_MODEL_3 = "gpt-3.5-turbo-0613"
GPT_MODEL_3_LONG = "gpt-4-32k-0314"
GPT_MODEL_4 = "gpt-4-0613"

client = OpenAI(api_key=api_key)


def generate_response(messages, functions, model, function_call):
    try:
        response = client.chat.completions.create(
            model = model,
            messages = messages,
            functions = functions,
            function_call = function_call
        )
        return response

    except Exception as e:
        logging.info(f"Exception: {e}, Unable to generate ChatCompletion response")


def get_message(chat_response):
    return chat_response.choices[0].message.content
