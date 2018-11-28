# Coding Challenge: Word count web application

## The task:

"Task Description
The web application should show a simple input form with a text field for entering a web site URL. The input form must contain a button for sending the entered URL to the server for processing.
On the server side, scrape the provided URL and extract the text of all paragraph (\<p>) elements. Count the word occurrences and send the top 20 words including their frequencies back to client. On the client side, display these results in a simple table.
In case the URL is not valid, or you encounter any other error while scraping the web site, display a proper error message on the client, including the HTTP status code and a user-friendly error message.
Provide a simple document where you describe how to build and run your solution. Also describe any decisions and assumptions you made while creating the solution."

### Requirements:

To run this code you'll first need to install all the packages mentioned in the requirements.txt file into your virtual environment.

To do this, run:

    $ pip3 install package

from your terminal

You'll then need to run

    $ export FLASK_APP=wordcountapplication.py
    $ flask run

to run the application.

Now all you need to do is open up "localhost:5000" in your browser and you'll be good to go!

## Explanations:

I had initially planned tackleing this exercise using TDD (Test Driven Development) but quickly realized it was going to take me a lot more time. Hence, this is my second take at this exercise.

My first steps were to create the basic files and folders included in pretty much every flask application:

wordcountapplication
    -> app
        -> templates
            -> base.html
        -> __init___.py (to indicate that app be treated as a package)
        -> routes.py (where I would later define my views)
    -> wordcountapplication.py

### The app folder

This folder contains the essence of the application.
In here I have a folder called "template" in which I've stored all the html templates to be rendered in the views functions.

The two html templates "count.html" and "index.html" inherit from the "base.html" which saves a lot of time. This basically means that the base template will always be rendered and will have specific sections where the code in "count.html" or "index.html" will be added.

The forms.py file will handle the form in which the url is entered
whose words need to be counted.

And finally routes.py is the view function which indicates what exactly should happen when a specific path is entered into the web browser.

### The configuration file

This file only contains 4 lines, as this is a really simple web app, but will be quite important in bigger projects

### That strange "obo.py" file

I'm going to be honest, this is my first time trying to web scrape.
I came across this website: https://programminghistorian.org/en/lessons/counting-frequencies
while trying to figure out how to do this and it seemed quite straight forward, with a few adjustments because I'm using Python3 instead of Python2.
However, with more time in hand, I most likely wouldn't use this. I am sure (or hope) there are better ways to web scrape, but this is what I could find and kind of implement in time.

## Conclusion:

Well, I've tried my best completing the challenge, and even still there are parts missing. I'll be continuing to work on this project for the rest of the day (and night, probably) because I'm having fun with it, but since I've been given limited time, here is what I have so far :)

## To do:

- handle errors
- fix table size
- refactor web scraper

## Resources:

https://programminghistorian.org/en/lessons/counting-frequencies <br>
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
