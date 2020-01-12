from flask import Flask, jsonify, request
from flask_cors import CORS
from process import processLabels

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/image', methods=['GET', 'POST'])
def receiveLabels():
    if request.method != 'POST':
        return jsonify("Payload failed")

    return jsonify(processLabels(request.data))

if __name__ == '__main__':
    app.run()
