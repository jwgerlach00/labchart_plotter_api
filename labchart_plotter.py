import flask
from flask import request

# Sourced from pypi.com/jwgerlach
import labchart_tools


app = flask.Flask(__name__)


@app.route('/plot', methods=['POST'])
def plot():
    if request.method == 'POST':
        data = request.get_json()
        text_data = data.text
        
        