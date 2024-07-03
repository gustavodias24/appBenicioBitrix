from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    args = request.args
    body = request.json

    return jsonify({
        "args": args,
        "body": body
    })


if __name__ == "__main__":
    app.run()
