import redis
import psycopg2
import time

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def count_words(text):
    return len(text.split())

while True:
    job = r.brpop("jobs", timeout=5)
    if job:
        text = job[1]
        wc = count_words(text)
        print(f"Processing: {text} -> {wc}")

        conn = psycopg2.connect(
            host="db",
            database="wordcounts",
            user="wc_user",
            password="wc_pass"
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO results(text, wordcount) VALUES (%s,%s);",
            (text, wc)
        )
        conn.commit()
        cur.close()
        conn.close()

    time.sleep(1)
