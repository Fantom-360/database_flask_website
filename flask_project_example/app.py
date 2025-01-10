from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index0.html")

@app.route("/support")
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