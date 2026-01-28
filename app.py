from flask import Flask, render_template, redirect, url_for
from components.data import file_types

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FILE_EXTRACTOR'

@app.route('/homepage')
def homepage():
    return render_template("index.html")

@app.route("/convert/<file_type>", methods=['GET', 'POST'])
def convert(file_type):
    return render_template("file.html", file_types=file_types, file_type=file_type)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return redirect('homepage')
