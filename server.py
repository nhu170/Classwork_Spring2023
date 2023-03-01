from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Serve On"


@app.route("/info", methods=["GET"])
def info_route():
    return "This server was written for BME547"


if __name__ == "__main__":
    app.run()
