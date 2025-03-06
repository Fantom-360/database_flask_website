from flask import Flask, render_template, request, redirect, flash, session, url_for
import hashlib
import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    database = "library"
)
cursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "something_meow"
# @app.route('/register', methods=["GET"])
# def test_something():
#     return "this rout func for only Get requests"

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confr_password = request.form.get("confirm_password")

        if password != confr_password:
            flash("Passwords do not match!", "error")
            return redirect("/register")
        
        #password_hash = hashlib.sha256(password.encode()).hexdigest()

        query = "INSERT INTO register (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)

        
        cursor.execute(query, values)
        mydb.commit()
        flash("you have sucessfuly registred", "success")
        return redirect("/login")
        
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        cursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM register WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and user["password"] == password:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            flash("login succesful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "error")
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("index0.html")

@app.route("/books")
def supp():
    return render_template("index1.html")

@app.route("/sign_up")
def sing():
    return render_template("index2.html")

@app.route("/log_in")
def login():
    return render_template("index3.html")

@app.route('/admin')
def admin():
    pass

if __name__ == "__main__":
    app.run(debug=True)