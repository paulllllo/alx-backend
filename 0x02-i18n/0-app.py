#!/usr/bin/env python3
"""ALX SE flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """prints hello world"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='5000', threaded=True)
