from flask import Flask, render_template, redirect, url_for
from components.data import file_types
from components.forms import DOCConvert, PDFConvert, TXTConvert, CSVConvert
from config import app_config

app = Flask(__name__)
app.config['SECRET_KEY'] = app_config

@app.route('/homepage')
def homepage():
    return render_template("index.html")

@app.route("/convert/<file_type>", methods=['GET', 'POST'])
def convert(file_type):
    user_upload = None
    doc_converter = DOCConvert()
    pdf_converter = PDFConvert()
    txt_converter = TXTConvert()
    csv_converter = CSVConvert()
    return render_template("file.html", file_types=file_types, file_type=file_type, doc_converter=doc_converter,
                           pdf_converter=pdf_converter, txt_converter=txt_converter, csv_converter=csv_converter,
                           user_upload=user_upload)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return redirect('homepage')
