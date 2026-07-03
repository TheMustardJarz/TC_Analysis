from flask import Flask, render_template
from odds_calculation import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    main()
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    calculater()
    return "Odds calculated"

if __name__ == "__main__":
    app.run(debug=True)