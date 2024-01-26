#!/usr/bin/env python3
"""ALX SE i18n"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """flask-babel config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

# Initialize and set default config for babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """prints hello world"""
    return render_template('3-index.html')


if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='5000', threaded=True)
