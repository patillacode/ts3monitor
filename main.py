import os

import ts3

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

TS3_SERVER = os.environ.get("TS3_SERVER")
TS3_USER = os.environ.get("TS3_USER")
TS3_PASS = os.environ.get("TS3_PASS")
DOCKER_EXPOSED_PORT = os.environ.get("DOCKER_EXPOSED_PORT")
DEBUG = bool(os.environ.get("DEBUG"))


@app.route("/status", methods=["GET", "HEAD"])
def status():
    return "ts3monitor is up and running!", 200


@app.route("/monitor", methods=["GET", "HEAD"])
def monitor():
    try:
        with ts3.query.TS3Connection(TS3_SERVER) as ts3conn:
            try:
                ts3conn.login(client_login_name=TS3_USER, client_login_password=TS3_PASS)
                ts3conn.use(sid=1)
                serverinfo = ts3conn.serverinfo()
                if serverinfo[0]["virtualserver_status"] == "online":
                    return "ts3 server is up and running!", 200
                else:
                    return "ts3 server is offline", 503

            except ts3.query.TS3QueryError as err:
                print("Error occurred:", err.resp.error["msg"])
                return "Error occurred", 503

    except Exception as err:
        print("Exception occurred:", err)
        return "Error", 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=DOCKER_EXPOSED_PORT, debug=DEBUG)
