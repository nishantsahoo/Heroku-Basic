from flask import render_template
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return("My name is Nishant Sahoo")

@app.route('/', methods=["POST"])
def my_page_result():
	return("Hello there!")

if __name__ == "__main__":
    app.run(debug=True)
