from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

client_scret = "io29XDkBsjeRkh4U2zpG0G5jhPJJBNKpybA29VsXqtS2woIDov"
client_id = "local.669bbb5f70bf42.85105579"


@app.route("/", methods=["POST"])
def my_handler():
    return jsonify({"funfando": request.json})


@app.route("/token")
def index():
    args = request.args

    code = args.get('code')

    url = (f"https://oauth.bitrix.info/oauth/token/?client_id={client_id}&client_secret"
           f"={client_scret}&code={code}&grant_type=authorization_code")

    response = requests.request("GET", url)

    return jsonify(response.json())


@app.route("/refresh")
def refresh():
    args = request.args

    refresh_token = args.get('refresh_token')

    url = (f"https://oauth.bitrix.info/oauth/token/?client_id={client_id}&client_secret"
           f"={client_scret}&refresh"
           f"_token={refresh_token}&grant_type=refresh_token")

    response = requests.request("GET", url)

    return jsonify(response.json())


# @app.route('/myhandler', methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
# def my_handler():
#     metodo_chamado = request.method
#     return jsonify({"funfando": "sim", "metodo_chamado": metodo_chamado})


if __name__ == "__main__":
    app.run()
