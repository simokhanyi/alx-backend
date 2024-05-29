#!/usr/bin/env python3
""" Flask app """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False


babel = Babel(app)
@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
