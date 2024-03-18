import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from function_calling.FunctionCalling import *
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates/")
messages = []
messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})


logging.basicConfig(filename="info.log",
                    filemode='a',
                    encoding='utf-8',
                    format='%(asctime)s %(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/get_prompt")
def get_prompt(prompt: Request):
    messages.append({"role": "user", "content": prompt})
    chat_response = generate_response(
        messages, functions, GPT_MODEL_3, "auto"
    )
    assistant_message = chat_response.choices[0].message
    messages.append(assistant_message)
    return templates.TemplateResponse('prompt.html', context={'request': prompt, 'result': assistant_message.content})


# @app.post("/prompt_response")
# def prompt_response(request: Request, result: str):
#     return templates.TemplateResponse('prompt.html', context={'request': request, 'result': result})


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
