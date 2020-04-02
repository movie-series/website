from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get("mycheckbox"))
        return 'jäs'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
