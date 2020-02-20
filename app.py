from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    movie = "Inception"

    return render_template("index.html", movie=movie)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
