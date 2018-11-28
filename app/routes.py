from flask import render_template
from app import app
from app.forms import WordForm


@app.route('/')
@app.route('/index')
def index():
    form = WordForm()
    return render_template('index.html', title='Word Count Application', form=form)