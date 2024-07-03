from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    args = request.args

    return jsonify({
        "args": args
    })


if __name__ == "__main__":
    app.run()
