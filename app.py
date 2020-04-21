from flask import Flask, render_template, request
from json import load
app = Flask(__name__)

with open("movies.json", "r") as f:
    movies = load(f)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        displayed = []
        if request.form.get("action"):
            displayed.extend(movies["action"])
        if request.form.get("comedy"):
            displayed.extend(movies["comedy"])
        if request.form.get("drama"):
            displayed.extend(movies["drama"])
        if request.form.get("scifi"):
            displayed.extend(movies["scifi"])
        if request.form.get("horror"):
            displayed.extend(movies["horror"])
        if request.form.get("thriller"):
            displayed.extend(movies["thriller"])
        if request.form.get("romance"):
            displayed.extend(movies["romance"])
        displayed = sorted(displayed, key=lambda k: k["rating"], reverse=True)
        return render_template('index.html', movies=displayed)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
