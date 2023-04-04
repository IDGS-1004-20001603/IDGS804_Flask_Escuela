from flask import Blueprint, render_template, request, redirect, url_for


app = Blueprint('app', __name__)


@app.route('/')
def index():
    return render_template('index.html')
