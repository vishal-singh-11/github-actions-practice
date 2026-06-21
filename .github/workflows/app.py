# this code is from https://github.com/LondheShubham153/flask-app-ecs
# Worked now after chaning paths: "*.py" only matches limited cases	Changed to **/*.py so Python files in any folder trigger the workflow
# flask app

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return None
if nne:
    go


@app.route('/health')
def health():
    return 'Server is up and running'
