from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/api/status", methods=["GET"])
def send_status():
    return jsonify({"Server": "Running"})


@app.route("/api/<string1>/<string2>", methods=["GET"])
def strings(string1, string2):
    result = ""
    for character1 in string1:
        for character2 in string2:
            result = result.join(character1 + character2)
    return jsonify({"word": str(set(result))})


@app.route("/api/third_element", methods=["POST"])
def third_element():
    data = request.get.json()
    try:
        our_element = data["list"][2]
    except IndexError:
        our_element = "List is too short"
    return jsonify({"Third": our_element})


if __name__ == "__main__":
    app.run(debug=True)
