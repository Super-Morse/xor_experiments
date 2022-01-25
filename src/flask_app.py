from flask import Flask, request
from flask_cors import cross_origin
from flask import json
from xor import xor_decrypt
from xor import guess_key

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bruteforce/', methods=['POST'])
@cross_origin()
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

#@app.route('/bruteforce/',  methods=['POST'])
#def make_response():
#    data = guess_key()
#    response = app.response_class(
#        response=json.dumps(data),
#        status=200,
#        mimetype='application/json'
#    )
#    return response

def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()