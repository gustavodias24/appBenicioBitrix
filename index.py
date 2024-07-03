from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    args = request.args

    code = args.get('code')

    url = (f"https://oauth.bitrix.info/oauth/token/?client_id=local.6684443e2eb8f5.18028528&client_secret"
           f"=5I0F06k4ZLXn9LV4pfcE4rUh24X2TRehm82taFsWKiExgKI075&code={code}&grant_type=authorization_code")

    response = requests.request("GET", url)

    return jsonify(response.json())


@app.route("/refresh")
def refresh():
    args = request.args

    refresh_token = args.get('refresh_token')

    url = (f"https://oauth.bitrix.info/oauth/token/?client_id=local.6684443e2eb8f5.18028528&client_secret"
           f"=5I0F06k4ZLXn9LV4pfcE4rUh24X2TRehm82taFsWKiExgKI075&refresh"
           f"_token={refresh_token}&grant_type=refresh_token")

    response = requests.request("GET", url)

    return jsonify(response.json())


if __name__ == "__main__":
    app.run()
