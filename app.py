import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    topics = [
        {"title": "Cybersecurity Basics", "img": "cyber1.jpg", "desc": "Learn the fundamentals of cybersecurity."},
        {"title": "Phishing Attacks", "img": "phishing.jpg", "desc": "How to recognize phishing emails and scams."},
        {"title": "Strong Passwords", "img": "cyber.jpg", "desc": "Tips for creating unbreakable passwords."},
        {"title": "Online Safety Tips", "img": "cyber.jpg", "desc": "Best practices for safe browsing."}
    ]
    return render_template("index.html", topics=topics)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")  # Make sure this file exists in templates/

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render sets the PORT automatically
    app.run(host="0.0.0.0", port=port)        # no debug=True here
