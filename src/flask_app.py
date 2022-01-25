from flask import Flask, request, json, jsonify
from flask_cors import cross_origin
from xor import xor_decrypt
from xor import guess_key

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bruteforce/', methods=['GET', 'POST'])
@cross_origin()
def process_json():
    if (request.method == 'POST'):
        content_type = request.headers.get('Content-Type')

        data = request.data
        values = json.loads(data)
        text = values['text']
        size = int(values['size'])
        text_list = text.split(',')
        map_object = map(int, text_list)
        list_of_integers = list(map_object)
        response_data = guess_key(list_of_integers, size)


        return jsonify(response_data), 200



    return request.method
    #content_type = request.headers.get('Content-Type')
    #if (content_type == 'application/json'):
        #json = request.json
        #return json
    #else:

#@app.route('/bruteforce/',  methods=['POST'])
#def make_response():
#        response=json.dumps(data),
#        status=200,
#        mimetype='application/json'
#    )
#    return response

def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()