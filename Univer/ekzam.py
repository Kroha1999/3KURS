from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/",methods=["GET"])
def wellcome():
    return "Wellcome to len system"

@app.route("/",methods=["POST"])
def getLen():
    text = request.json['text']
    return "Length of your text = "+ str(len(text)) + "\nLength of your text without spaces = " + str(len(text.replace(" ","")))


if __name__ == "__main__":
    app.run(port = 8080)
