from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        reflection = request.form["reflection"]
        mood = request.form["mood"]
        productivity = request.form["productivity"]

        print("Reflection:", reflection)
        print("Mood:", mood)
        print("Productivity:", productivity)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)