#!/usr/bin/env python3
""" Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    login_as = request.args.get('login_as')
    if login_as:
        try:
            user_id = int(login_as)
            return users.get(user_id)
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    g.user = get_user()


@app.route('/')
def index():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
