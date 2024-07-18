from flask import Flask, render_template, request, url_for, redirect, session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = "PASSWORD"

fortunes = [
    "You will have a terrible day!",
    "Today you will meet someone important.",
    "Today is your lucky day!",
    "You will eat an apple today.",
    "You will sit on a chair today.",
    "You will have to protect yourself.",
    "You will find your phone.",
    "You will go to sleep late.",
    "Bad news is coming your way.",
    "You will have problems with your code."
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_session['name'] = request.form['username']
        login_session['birthmonth'] = request.form['birthmonth']
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    name = login_session.get('name')
    return render_template('home.html', name=name)

@app.route('/fortune', methods=['GET'])
def fortune():
    if 'birthmonth' not in login_session:
        return redirect(url_for('login'))

    birthmonth = login_session['birthmonth']
    index = len(birthmonth) - 1

    if index > 9:
        chosen_fortune = fortunes[8] 
    else:
        chosen_fortune = fortunes[index]

    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)
