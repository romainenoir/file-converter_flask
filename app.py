from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FILE_EXTRACTOR'


@app.route('/homepage')
def homepage():
    return render_template("index.html")

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    return render_template("file.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return redirect('homepage')

if __name__ == "__main__":
    app.run(debug=True)