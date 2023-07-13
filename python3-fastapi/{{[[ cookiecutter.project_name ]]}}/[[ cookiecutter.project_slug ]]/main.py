from fastapi import FastAPI

[[ cookiecutter.project_slug ]]_app = FastAPI()

@[[ cookiecutter.project_slug ]]_app.get("/")
def main():
    return "hello world"