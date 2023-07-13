from flask import Flask

[[ cookiecutter.project_slug ]]_app = Flask(__name__)

@[[ cookiecutter.project_slug ]]_app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"