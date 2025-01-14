from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route("/")
def gome():
    message = "welcome to Flask App, nya~!"
    return render_template("index.html", greeting = message)






if __name__ == "__main__":
    app.run(debug=True)