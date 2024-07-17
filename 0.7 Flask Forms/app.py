from flask import Flask, render_template, request, url_for, redirect
import random

app = Flask(__name__)

@app.route('/home',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('fortune',birthmonth = request.form['birthmonth']))
        

    return render_template('home.html')

@app.route('/fortune/<string:birthmonth>')
def fortune(birthmonth):
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
    index = len(birthmonth) - 1
    if index > 9:
        chosen_fortune = fortunes[8]
    else:
        chosen_fortune = fortunes[index]
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)