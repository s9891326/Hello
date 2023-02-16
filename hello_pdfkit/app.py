import pdfkit
from htmlwebshot import WebShot

from flask import send_file
from flask import Flask
from flask import render_template

app = Flask(__name__)

SHOT = WebShot()
SHOT.quality = 100


@app.route('/')
def index():
    a = render_template('hello.html', test=123456)

    image = SHOT.create_pic(html=a, output="shot.jpg")

    # https://github.com/twtrubiks/python-pdfkit-example
    pdfkit.from_string(a, 'sample.pdf')
    # return a
    return send_file("shot.jpg", mimetype="image/jpg")


if __name__ == '__main__':
    app.debug = True
    app.run()
