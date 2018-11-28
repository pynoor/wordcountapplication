
# In this file we're going to define the functions that will be
# executed, depending on which url path is being requested.


from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import WordForm
import requests
from requests.exceptions import MissingSchema
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
        try:
            response = requests.get(url)
        except MissingSchema:
            return render_template('error.html', error=
            "Doesn't look like it!")
        if response.status_code != 200:
            return render_template('error.html', error="Your submission caused a " +
            str(response.status_code) + " error.")

        html = response.content.decode("utf-8")
        text = obo.stripTags(html).lower()
        fullwordlist = obo.stripNonAlphaNum(text)
        wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
        dictionary = obo.wordListToFreqDict(wordlist)
        sorteddict = obo.sortFreqDict(dictionary)[:21]
        return render_template('results.html', result=sorteddict)
    return render_template('count.html', title='Word Count Application', form=form)