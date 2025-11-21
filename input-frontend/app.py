from flask import Flask, render_template, request
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        r.lpush("jobs", text)
        return render_template("index.html", message="Submitted successfully!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
