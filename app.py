from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Cloudwala Banda'

@app.route('/health')
def health():
    return 'Server is up and running'
