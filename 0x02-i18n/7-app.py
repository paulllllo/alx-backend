#!/usr/bin/env python3
"""ALX SE i18n"""
from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets the current mocked logged in user or None if not found"""
    login_as = request.args.get('login_as')
    if not login_as:
        return None
    user_id = int(login_as)
    try:
        return users[user_id]
    except KeyError:
        return None


@app.before_request
def before_request():
    """Execution to take place before any request is made"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages"""
    locale = request.args.get('locale')
    if locale:
        return locale
    user = get_user()
    if user and (user["locale"] == 'en' or user["locale"] == 'fr'):
        return user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Get timezone from url parameter"""
    time_zone = request.args.get('timezone')
    if time_zone:
        try:
            tzone = pytz.timezone(time_zone)
            return tzone.zone
        except pytz.exceptions.UnKnownTimeZoneError:
            return None

    if g.user:
        time_zone = g.user.get('timezone')
        try:
            tzone = pytz.timezone(time_zone)
            return tzone.zone
        except pytz.exceptions.UnKnownTimeZoneError:
            return None


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """Renders a welcome message in the browser"""
    return render_template('7-index.html')


if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='5000', threaded=True)
