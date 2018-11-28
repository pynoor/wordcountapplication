
# In this file we're going to define the functions that will be
# executed, depending on which url path is being requested.


from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import WordForm
import requests
import obo


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/count', methods=['GET', 'POST'])
def count():
    form = WordForm()
    if form.validate_on_submit():
        url = form.url.data
        response = requests.get(url)
        html = response.content.decode("utf-8")
        text = obo.stripTags(html).lower()
        fullwordlist = obo.stripNonAlphaNum(text)
        wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
        dictionary = obo.wordListToFreqDict(wordlist)
        sorteddict = obo.sortFreqDict(dictionary)
        for s in sorteddict[:21]:
            flash(str(s))
        return redirect(url_for('index'))
    return render_template('count.html', title='Word Count Application', form=form)