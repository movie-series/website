from flask import Flask, render_template, request
from json import load
app = Flask(__name__)

with open("movies.json", "r") as f:
    movies = load(f)

print(movies["action"][0]["title"])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        print(request.form.get("action"))
        print(request.form.get("comedy"))
        print(request.form.get("drama"))
        print(request.form.get("scifi"))
        print(request.form.get("horror"))
        print(request.form.get("thriller"))
        print(request.form.get("romance"))
        return render_template('index.html', movies=movies)

    return render_template('index.html')

movies = [
    {
        "name": "Interstellar",
        "link": "https://www.imdb.com/title/tt0816692/?ref_=nv_sr_srsg_0"
    },
    {
        "name": "Gladiator",
        "link": "https://www.imdb.com/title/tt0172495/?ref_=fn_al_tt_1"
    }
]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
