from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

client_scret = "4d68Z5SJ7ElR15ZP5MmRcFgjAIjStw1ssPBTxEWBD7rJBed4s7"
client_id = "local.66d1c791da7085.38798748"


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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
