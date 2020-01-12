from flask import Flask, jsonify, request
from flask_cors import CORS
from process import *

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hello_world():
    getList()
    return 'Hello World!'


@app.route('/image', methods=['GET', 'POST'])
def receiveLabels():
    if request.method != 'POST':
        return jsonify("Payload failed")

    return processLabels(request.data)


@app.route('/labellist')
def get_label_list():
    return jsonify({'labels': getList()})


if __name__ == '__main__':
    app.run()
