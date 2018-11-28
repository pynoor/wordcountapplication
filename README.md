# Coding Challenge: Word count web application

## The task:

"Task Description
The web application should show a simple input form with a text field for entering a web site URL. The input form must contain a button for sending the entered URL to the server for processing.
On the server side, scrape the provided URL and extract the text of all paragraph (<p>) elements. Count the word occurrences and send the top 20 words including their frequencies back to client. On the client side, display these results in a simple table.
In case the URL is not valid, or you encounter any other error while scraping the web site, display a proper error message on the client, including the HTTP status code and a user-friendly error message.
Provide a simple document where you describe how to build and run your solution. Also describe any decisions and assumptions you made while creating the solution."

### Requirements:

To run this code you'll first need to install all the packages mentioned in the requirements.txt file into your virtual environment.

(To do this, run:
$ pip3 install package
from your terminal)

You'll then need to run

$ export FLASK_APP=wordcountapplication.py
$ flask run

to run the application.

Now all you need to do is open up "localhost:5000" in your browser and you'll be good to go!

## Explanations:



## Resources:

https://programminghistorian.org/en/lessons/counting-frequencies
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
