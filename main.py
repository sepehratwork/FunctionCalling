from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from function_calling import FunctionCalling


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/get_prompt")
def get_prompt(prompt: Request):
    result = ""
    return templates.TemplateResponse('prompt.html', context={'request': prompt, 'result': result})


@app.post("/prompt_response")
def prompt_response(request: Request, result: str):
    result = FunctionCalling.get_response(result)
    return templates.TemplateResponse('prompt.html', context={'request': request, 'result': result})
