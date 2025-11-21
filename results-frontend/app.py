from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_data():
    conn = psycopg2.connect(
        host="db",
        database="wordcounts",
        user="wc_user",
        password="wc_pass"
    )
    cur = conn.cursor()
    cur.execute("SELECT text, wordcount FROM results ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route("/")
def index():
    data = get_data()
    return render_template("results.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
