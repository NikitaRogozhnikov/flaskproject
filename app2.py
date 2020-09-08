from flask import Flask, render_template, url_for,request, redirect
from flask_mail import Mail, Message
app=Flask(__name__)

github_link=""
instagram_link=""
facebook_link=""



donate_link=""
app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_DEFAULT_SENDER'] = ''
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)



@app.route("/")
@app.route("/about")
def index():
	return render_template("about.html")


@app.route("/feedback",methods=["POST","GET"])
def feedback():
	if request.method=="POST":
		print(request.form["username"])
		sendmsg()
	return render_template("feedback.html")

@app.route("/donate",methods=["POST","GET"])
def donate (donate_link=donate_link):
	return render_template("donate.html",link=donate_link)


@app.route("/github")
def redirect_github():
	return redirect(github_link)
@app.route("/facebook")
def redirect_facebook():
	return redirect(facebook_link)
@app.route("/instagram")
def redirect_instagram():
	return redirect(instagram_link)


def sendmsg():
	mes=request.form["message"]+'\n'+"Contact me: \n"+request.form["username"]+'\n'+request.form["email"]
	msg = Message("From Niro.com",  recipients=['nikitarzhn95@gmail.com'])
	msg.body=mes
	mail.send(msg)

if __name__ == "__main__":
	app.debug=True
	app.run()
