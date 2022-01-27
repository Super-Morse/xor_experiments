from flask import Flask, jsonify, make_response, request, json
from xor import guess_key

app = Flask(__name__)

@app.route('/bruteforce/', methods=['POST'])
def bruteforce():
    '''Reply to incoming POST with possible combinations of key and decrypted text found using guess_key function from xor.py'''

    data = request.data
    values = json.loads(data)
    text = values['text']
    size = int(values['size'])
    text_list = text.split(',')
    map_object = map(int, text_list)
    list_of_integers = list(map_object)
    response_data = guess_key(list_of_integers, size)
    resp = make_response(jsonify(response_data), 200)

    # This fix CORS issues with different ports between UI and backend
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == '__main__':
    app.run()
