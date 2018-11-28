from flask import render_template, flash, redirect
from app import app
from app.forms import WordForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Word Count Application')


@app.route('/count', methods=['GET', 'POST'])
def count():
    form = WordForm()
    if form.validate_on_submit():
        flash('Counting the word {}.'.format(form.word.data))
        return redirect('/index')
    return render_template('count.html', title='Word Count Application', form=form)