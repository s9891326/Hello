import pdfkit

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    a = render_template('hello.html', test=123456)
    # https://github.com/twtrubiks/python-pdfkit-example
    pdfkit.from_string(a, 'sample.pdf')
    return a


if __name__ == '__main__':
    app.debug = True
    app.run()
