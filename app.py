from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Create Database and Table
def init_db():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reflections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reflection TEXT,
            mood TEXT,
            productivity INTEGER
        )
    """)

    conn.commit()
    conn.close()


# Homepage Route
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        reflection = request.form["reflection"]
        mood = request.form["mood"]
        productivity = request.form["productivity"]

        conn = sqlite3.connect("database.db")

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO reflections
            (reflection, mood, productivity)
            VALUES (?, ?, ?)
        """, (reflection, mood, productivity))

        conn.commit()
        conn.close()

        print("Reflection saved successfully!")

    return render_template("index.html")


# Run App
if __name__ == "__main__":

    init_db()

    app.run(debug=True)