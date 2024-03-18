from openai import OpenAI
import requests
# from tenacity import retry, wait_random_exponential, stop_after_attempt
# from termcolor import colored 
from function_calling import functions


api_key="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"

# GPT_MODEL_3 = "gpt-3.5-turbo-0125"
GPT_MODEL_3 = "gpt-3.5-turbo-0613"
GPT_MODEL_3_LONG = "gpt-4-32k-0314"
GPT_MODEL_4 = "gpt-4-0613"

client = OpenAI(api_key=api_key)

def get_response(user_prompt, functions, model, function_call):
    try:
        response = client.chat.completions.create(
            model = model,
            messages = [{'role': 'user', 'content': user_prompt}],
            functions = functions.functions,
            function_call = function_call
        )
        return response.choices[0].message.function_call.arguments
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")


def generate_response(user_prompt):
    output = get_response(user_prompt, functions, model=GPT_MODEL_3, function_call="auto")
    return output
