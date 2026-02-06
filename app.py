from flask import Flask, render_template, redirect, send_file
from components.data import file_types
from components.forms import DOCConvert, PDFConvert, TXTConvert, CSVConvert
from components.functions import PDF_CONVERT
from config import app_config_key

app = Flask(__name__)
app.config['SECRET_KEY'] = app_config_key

@app.route('/homepage')
def homepage():
    return render_template("index.html")

@app.route("/convert/<file_type>", methods=['GET', 'POST'])
def convert(file_type):
    file_type = file_type.upper()
    user_upload = None
    doc_converter = DOCConvert()
    pdf_converter = PDFConvert()
    txt_converter = TXTConvert()
    csv_converter = CSVConvert()
    
    if pdf_converter.validate_on_submit():
        convert_pdf_ = PDF_CONVERT()
        user_upload = pdf_converter.file_doc.data
        
        # CONVERT PDF TO TXT & SEND BACK TO USER
        if pdf_converter.convert_to_txt.data:
            file_stream, file_name_title = convert_pdf_.PDF_to_TXT(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif pdf_converter.convert_to_doc.data:
            file_stream, file_name_title = convert_pdf_.PDF_to_DOC(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif pdf_converter.convert_to_csv.data:
            pass
    elif txt_converter.validate_on_submit():
        user_upload = txt_converter.file_doc.data
        pass
    elif csv_converter.validate_on_submit():
        user_upload = csv_converter.file_doc.data
        pass
    
    return render_template("file.html", file_types=file_types, 
                           file_type=file_type, 
                           doc_converter=doc_converter,
                           pdf_converter=pdf_converter, 
                           txt_converter=txt_converter, 
                           csv_converter=csv_converter,)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return redirect('homepage')
