from flask import Flask

app = Flask(__name__)

from app import routes, models


@app.route("/")
def hell():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
