from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get("mycheckbox"))
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
