import simplejson as json
from flask import render_template
from flask import Flask, request, send_from_directory
from bs4 import BeautifulSoup
import mechanize
import string

app = Flask(__name__)

@app.route("/")
def home():
    return "My name is Nishant Sahoo"
    # return render_template("home.html", name="home")

@app.route('/', methods=["POST"])
def my_page_result():
	return "Hello there!"

if __name__ == "__main__":
    app.run(debug=True)
