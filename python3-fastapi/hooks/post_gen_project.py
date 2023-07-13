import os
import shutil

# {% raw %}
# raw block it's necessary to disable jinja2
# from parsing the curly brackets
jvss = "{{"  # jinja_variable_start_string
jves = "}}"  # jinja_variable_end_string
# {% endraw %}

# when we don't use jinja2 default delimiters 
# we have to rename the project main folder after generating
# more information on https://github.com/cookiecutter/cookiecutter/issues/1736
os.system(f"cd .. && mv ./{jvss}{{ cookiecutter.project_name }}{jves} {{ cookiecutter.project_name }}")
