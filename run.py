from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Memory Games API!"


@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "You got it!"})


if __name__ == "__main__":
    app.run(debug=True)
