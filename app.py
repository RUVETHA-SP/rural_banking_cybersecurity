from flask import Flask, render_template, request

from fraud_detection.fraud_detection import check_fraud
from phishing_detection.phishing_checker import check_phishing

app = Flask(__name__)

balance = 50000


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def user_login():

    username = request.form["username"]

    return render_template(
        "dashboard.html",
        user=username,
        balance=balance
    )


@app.route("/transfer", methods=["POST"])
def transfer():

    global balance

    amount = int(request.form["amount"])

    fraud = check_fraud(amount)

    if fraud:
        alert = "⚠ Suspicious transaction detected!"
    else:
        alert = "Transaction completed successfully"

    balance -= amount

    return render_template(
        "dashboard.html",
        user="User",
        balance=balance,
        alert=alert
    )


@app.route("/check_link", methods=["POST"])
def check_link():

    url = request.form["url"]

    phishing = check_phishing(url)

    if phishing:
        alert = "⚠ Phishing link detected!"
    else:
        alert = "Link appears safe"

    return render_template(
        "dashboard.html",
        user="User",
        balance=balance,
        alert=alert
    )


if __name__ == "__main__":
    app.run(debug=True)