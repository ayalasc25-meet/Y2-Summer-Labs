from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase


app = Flask(__name__, templates_folder='templates', static_folder = 'static')
app.config['SECRET_KEY'] = "PASSWORD"

firebaseConfig = {

  'apiKey': "AIzaSyCdMWdLHLHUDk3mTRlqT3VSZuT0QeeaB0o",

  'authDomain': "authentication-lab-7e1ff.firebaseapp.com",

  'projectId': "authentication-lab-7e1ff",

  'storageBucket': "authentication-lab-7e1ff.appspot.com",

  'messagingSenderId': "1088116653430",

  'appId': "1:1088116653430:web:d4b6dc18c5f0a1342a8e57",

  'measurementId': "G-YD5X1BD7HL"

}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            login_session['quotes']=[]
            return redirect(url_for('home'))
        except:
            error = "Didn't work, sorry"
            return render_template("login.html", error=error)

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'GET':
        return render_template("signin.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
        	login_session['quotes']=[]
            return redirect(url_for('home'))
        except:
            error = "Didn't work, sorry"
            return render_template("signup.html",error=error)
        
@app.route('/thanks', methods=["GET", "POST"])
def thanks():
    if request.method == 'GET':
        return render_template("thanks.html") 
    

@app.route('/display', methods=["GET", "POST"])
def display():
    if request.method == 'GET':
        return render_template("display.html") 
  


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)