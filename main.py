from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/get_prompt")
def get_prompt(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('prompt.html', context={'request': request, 'result': result})


# @app.post("/prompt_response")
# def prompt_response(request: Request, num: int = Form(...)):
#     result = spell_number(num)
#     return templates.TemplateResponse('prompt.html', context={'request': request, 'result': result})
