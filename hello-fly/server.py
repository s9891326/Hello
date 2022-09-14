from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Python Flask fly.io !"

if __name__ == '__main__':
    app.run()
