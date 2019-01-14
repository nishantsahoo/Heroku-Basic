from flask import Flask
import smtplib
app = Flask(__name__)

@app.route('/')
def homepage():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	#Next, log in to the server
	server.starttls()
	server.login("", "")

	#Send the mail
	msg = "Yo"
	server.sendmail("", "", msg)
    return("Hello!")

@app.route('/', methods=['POST'])
def sendmail():
	if not request.form['body']:
		return "Please enter some data"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	#Next, log in to the server
	server.starttls()
	server.login("", "")

	# Send the mail
	msg = request.form['body']
	server.sendmail("", "", msg)
	return("Mail sent with post message!")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)