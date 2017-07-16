from flask import Flask, render_template, request, redirect, flash, session
import re
import time

app = Flask(__name__)

app.secret_key = "V12Zr47j\3yX R~X@Hu0|q\9!jmM]Lwf/,?KTW%"

EMAIL_REGX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def validation():
	if len(request.form["fname"]) < 1:
		flash("Name cannot be empty!", "error")

	if len(request.form["lname"]) < 1:
		flash("Name cannot be empty!", "error")

	if not EMAIL_REGX.match(request.form["email"]):
		flash("You have entered an Invalid Email!!!", "error")

	elif  EMAIL_REGX.match(request.form["email"]):
		flash("Success!!!", "error")

	if len(request.form["pw"]) < 1:
		flash("Please enter your password!!!", "error")

	if len(request.form["pw"]) < 8 and len(request.form["pw"]) == len(request.form["cpw"]):
		flash("Password must be at least 8 Characters!!!", "error")
	elif len(request.form["pw"]) != len(request.form["cpw"]):
		flash("Password does not match!!!", "error")

		#Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value
	for index in request.form["pw"]:
		if index.isupper() == False and  index.isdigit() == False:
			flash("Password must have at least 1 uppercase letter and 1 numeric value.", "error")

		#Add a birth-date field that must be validated as a valid date (and must be from the past).
	if not time.strptime(request.form["birthDay"], "%Y-%m-%d"):
		flash("Only for those who were born in year 2000!!!", "error" )
	else:
		flash("Thanks for submitting your Information!!!", "error")

		print request.form["birthDay"]
		print type(request.form["birthDay"])
	return redirect("/")

app.run(debug=True)

