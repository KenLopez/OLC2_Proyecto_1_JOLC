from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/Compile")
def compile(message=''):
    return render_template('index.html', message=message)

@app.route("/")
def index():
    return redirect("Compile")

if __name__ == '__main__':
    app.run(debug=True)
