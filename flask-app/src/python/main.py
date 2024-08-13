import os
from flask import Flask, send_from_directory

app = Flask(__name__)

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')



@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/files/<path:filename>')
def get_file(filename):
    return send_from_directory(static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080)
