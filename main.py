from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/index", methods=['POST'])
def hello():
     return render_template('response.html')

@app.route("/checkname", methods=['POST'])

def error():
     username = request.form['username']
     nameerror = ""
     name_error = request.form['username']
     if name_error == "":
          name_error = "Please enter a valid username."
     
     for char in name_error:
          if char == " ":
               nameerror = "No spaces in Username please."

     if (len(name_error) > 20) or (len(name_error) < 3):
          nameerror = "Please enter a Username between 3 to 20 characters."

     passerror = ""
     matcherror = ""
     original = request.form['password']
     secondary = request.form['verify']
     if original != secondary:
          matcherror = "Your passwords did not match."
     
     if (len(original) > 20) or (len(original) <3):
          passerror = "Please enter a Password between 3 to 20 characters."
          

     email = request.form['email']
     email_error = ""

     if "@" not in email:
          email_error = "Please must contain a '@' and a '.'."
     
     if "." not in email:
          email_error = 'Email must contain a "." and a "@".'

     for char in email:          
          if char == " ":
               email_error = "Email cannot contain spaces."
          
     if (len(email) > 30) or (len(email) < 3):
          email_error = "Email length is not correct. Must be between 3 to 30 characters."

     if email == "":
          email_error = ""
                         
     if nameerror == "" and passerror == "" and matcherror == "" and email_error == "":
          officialname = request.form['username']
          return render_template("response.html", officialname = officialname)
     else:
          return render_template("get-username.html", username = username, nameerror = nameerror, passerror = passerror, matcherror = matcherror, email_error = email_error, email = email)

@app.route("/")
def index():
    
    return render_template('get-username.html')

app.run()