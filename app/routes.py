
# In this file we're going to define the functions that will be
# executed, depending on which url path is being requested.


import requests
from bs4 import BeautifulSoup
from flask import flash, redirect, render_template, url_for
from requests.exceptions import MissingSchema

import obo
from app import app
from app.forms import WordForm


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
        soup = BeautifulSoup(html, 'html.parser')
        text_in_paragraphs = str(soup.find_all('p'))
        text_within_paragraphs = obo.stripTags(text_in_paragraphs).lower()
        fullwordlist = obo.stripNonAlphaNum(text_within_paragraphs)
        wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
        dictionary = obo.wordListToFreqDict(wordlist)
        sorteddict = obo.sortFreqDict(dictionary)[:21]
        return render_template('results.html', result=sorteddict)
    return render_template('count.html', title='Word Count Application', form=form)