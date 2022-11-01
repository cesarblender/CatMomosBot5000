from flask import Flask


def startServer():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "ok"

    app.run(port=80, host="0.0.0.0", debug=False)
