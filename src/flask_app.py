from flask import Flask
from xor import xor_decrypt
from xor import guess_key

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()