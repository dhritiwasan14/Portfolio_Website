from flask import Flask, render_template, flash, redirect, url_for, session, logging
from wtforms.fields.html5 import EmailField
from wtforms import Form, StringField, TextAreaField, validators
from flask import request
from wtforms.widgets import TextArea
from firebase.firebase import FirebaseApplication
import json


url = "https://test-e691e.firebaseio.com/"
token = "6e9OXbho2b4mNli191mXBIUVWWI59xWfP6M8vQwk"

firebase = FirebaseApplication(url, token)

app = Flask(__name__)


class RegisterForm(Form):
	username = StringField(" ", [validators.Length(min=5, max=10)])
	email = EmailField(" ", [validators.Length(min=5, max=10)])
	message = TextAreaField(" ", widget=TextArea())

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/home.html")
def home_center():
    return render_template('home.html')

@app.route("/education.html")
def education():
    return render_template('education.html')

@app.route("/projects.html")
def projects():
    return render_template('projects.html')

@app.route("/contact.html", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        form = RegisterForm(request.form)
        return render_template('contact.html', form=form)
    else:
        
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']
        data = {'email': email, 'message': message}
        sent = json.dumps(data)
        result = firebase.post("/"+username, sent)
        print(result)
        return redirect('/')

def viewGithub():
    print('hurts sometime')

if __name__ == '__main__':
    app.run(host="0.0.0.0")