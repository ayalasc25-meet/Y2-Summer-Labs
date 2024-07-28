from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder = 'static')
app.config['SECRET_KEY'] = "PASSWORD"

firebaseConfig = {

  'apiKey': "AIzaSyD81syzBM73Ge6GedNgApLcdEExhL1XYcA",

  'authDomain': "personalprojecty2.firebaseapp.com",

  'databaseURL': "https://personalprojecty2-default-rtdb.europe-west1.firebasedatabase.app",

  'projectId': "personalprojecty2",

  'storageBucket': "personalprojecty2.appspot.com",

  'messagingSenderId': "1071005887784",

  'appId': "1:1071005887784:web:d931f51ea385a4a135741d",

  'databaseURL': "https://personalprojecty2-default-rtdb.europe-west1.firebasedatabase.app/"

}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db =firebase.database()

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else:
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user_id = login_session['user']['localId']
            return redirect(url_for('home'))
        except:
            error = "Umm, that didn't work. Try again"
            print(error)
            return render_template("signup.html",error=error)



@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Didn't work, sorry. Try again"
            print(error)
            return render_template("login.html",error=error)

@app.route('/signout', methods=["GET", "POST"])
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('login'))

@app.route('/myrecipes', methods=["GET", "POST"])
def myrecipes():
    try:
        user_id = login_session['user']['localId']
        userrecipes=db.child('users').child(user_id).child('recipes').get().val().values()
        print(userrecipes)
        return render_template("myrecipes.html", userrecipes=userrecipes)
    except:
        error = "Didn't work, sorry. Try again"
        print(error)
        return render_template("myrecipes.html",error=error)


@app.route('/addrecipe', methods=["GET", "POST"])
def addrecipe():
    if 'user' not in login_session:
        return redirect(url_for('login')) 
    if request.method == 'GET':
        return render_template("addrecipe.html")
    else: 
        try:
            user_id = login_session['user']['localId']
            recipe = {
                "namerecipe": request.form['namerecipe'],
                "recipe": request.form['recipe'],
                "recipetype":request.form['recipetype']
            }
            db.child('users').child(user_id).child('recipes').push(recipe)
            return render_template("thanks.html")
        except Exception as e:
            print(f"Error adding recipe: {str(e)}")
            return render_template("addrecipe.html", error="Failed to add recipe. Please try again.")


@app.route('/desserts', methods=['GET', 'POST'])
def desserts():
    try:
        all_desserts = []
        users = db.child('users').get().val()
        for user_id, user_data in users.items():
            if 'recipes' in user_data:
                for recipe_id, recipe in user_data['recipes'].items():
                    if recipe.get('recipetype') == 'dessert':
                        all_desserts.append(recipe)
        print("Desserts to be showed:", all_desserts)
        return render_template("desserts.html", desserts=all_desserts)
    except:
        error = "Didn't work, sorry. Try again"
        print(error)
        return render_template("home.html",error=error)

@app.route('/maincourse', methods=['GET', 'POST'])
def maincourse():
    try:
        all_maincourse = []
        users = db.child('users').get().val()
        for user_id, user_data in users.items():
            if 'recipes' in user_data:
                for recipe_id, recipe in user_data['recipes'].items():
                    if recipe.get('recipetype') == 'maincourse':
                        all_maincourse.append(recipe)
        print("Maincourses to be showed:", all_maincourse)
        return render_template("maincourse.html", maincourses=all_maincourse)
    except:
        error = "Didn't work, sorry. Try again"
        print(error)
        return render_template("home.html",error=error)

@app.route('/appetizer', methods=['GET', 'POST'])
def appetizer():
    try:
        all_appetizer = []
        users = db.child('users').get().val()
        for user_id, user_data in users.items():
            if 'recipes' in user_data:
                for recipe_id, recipe in user_data['recipes'].items():
                    if recipe.get('recipetype') == 'appetizer':
                        all_appetizer.append(recipe)
        print("Maincourses to be showed:", all_appetizer)
        return render_template("appetizer.html", appetizers=all_appetizer)
    except:
        error = "Didn't work, sorry. Try again"
        print(error)
        return render_template("home.html",error=error)


@app.route('/other', methods=['GET', 'POST'])
def other():
    try:
        all_other = []
        users = db.child('users').get().val()
        for user_id, user_data in users.items():
            if 'recipes' in user_data:
                for recipe_id, recipe in user_data['recipes'].items():
                    if recipe.get('recipetype') == 'other':
                        all_other.append(recipe)
        print("Others to be showed:", all_other)
        return render_template("other.html", others=all_other)
    except:
        error = "Didn't work, sorry. Try again"
        print(error)
        return render_template("home.html",error=error)

if __name__ == '__main__':
    app.run(debug=True)