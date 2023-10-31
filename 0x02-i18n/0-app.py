#!/usr/bin/env python3
"""Flask application"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Defines the home route"""
    return render_template('index.html')
