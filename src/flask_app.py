from flask import Flask, request, json, jsonify
from flask_cors import cross_origin
from xor import guess_key

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bruteforce/', methods=['GET', 'POST'])
@cross_origin()
def process_json():
    if (request.method == 'POST'):

        data = request.data
        values = json.loads(data)
        text = values['text']
        size = int(values['size'])
        text_list = text.split(',')
        map_object = map(int, text_list)
        list_of_integers = list(map_object)
        response_data = guess_key(list_of_integers, size)


        return jsonify(response_data), 200


if __name__ == '__main__':
    app.run()