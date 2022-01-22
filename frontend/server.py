from flask import Flask, jsonify, make_response
app = Flask(__name__)

@app.route('/bruteforce/', methods=['POST'])
def bruteforce():
    # Todo: make this method return with the possible encryptions
    resp = make_response(jsonify([["aa", "a@#sdf asd"], ["ab", "ad@!!#dv"]]))

    # This fix CORS issues with different ports between UI and backend
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()
