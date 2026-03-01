from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    current_usage = random.randint(50, 300)
    predicted_usage = current_usage + random.randint(-20, 40)
    return render_template("dashboard.html",
                           current=current_usage,
                           predicted=predicted_usage)

if __name__ == "__main__":
    app.run(debug=True)
