from flask import Flask, jsonify, make_response, request, json
from xor import guess_key

app = Flask(__name__)

@app.route('/bruteforce/', methods=['POST'])
def bruteforce():
    '''Reply to incoming POST with possible combinations of key and decrypted text found using guess_key function from xor.py'''


    values = json.loads(request.data)
    size = int(values['size'])
    text_list = list(map(int, values['text'].split(',')))
    response_data = guess_key(text_list, size)
    resp = make_response(jsonify(response_data), 200)

    # This fix CORS issues with different ports between UI and backend
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == '__main__':
    app.run()
