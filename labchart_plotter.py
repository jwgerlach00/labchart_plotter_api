import flask
from flask import request
from flask_cors import CORS

# Sourced from pypi.com/jwgerlach
from labchart_tools import LCDataViewer


app = flask.Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        viewer = LCDataViewer(file)
        return {
            'header': viewer.trial_data[0].columns.values.tolist()
        }


if __name__ == '__main__':
    app.run(debug=True)
