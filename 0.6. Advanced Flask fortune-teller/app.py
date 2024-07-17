from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fortune')
def fortune():
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
    chosen_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)