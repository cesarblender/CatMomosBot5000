from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi"

def start_server():
    app.run()
