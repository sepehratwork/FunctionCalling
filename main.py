from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from function_calling import FunctionCalling
import uvicorn


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
    result = FunctionCalling.generate_response(result)
    return templates.TemplateResponse('prompt.html', context={'request': request, 'result': result})


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
