#!/usr/bin/env python3
"""Flask application"""
from flask_babel import Babel
from flask import Flask, render_template, request


babel = Babel(app)


class Config(object):
    """Babel Configuration for the flask application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
#babel = Babel(app)


@babel.localselector
def get_locale() -> str:
    """function selects the best match for the supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    """Defines and returns the home route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
