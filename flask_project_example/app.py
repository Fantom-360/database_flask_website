from flask import Flask, render_template, session

app = Flask(__name__)
@app.route('/')
def rerout():
    return Flask.redirect('home')

@app.route("/home")
def home():
    return render_template("index0.html")

@app.route("/tables")
def supp():
    return render_template("index1.html")

@app.route("/sign_up")
def sing():
    return render_template("index2.html")

@app.route("/log_in")
def login():
    return render_template("index3.html")













if __name__ == "__main__":
    app.run(debug=True)