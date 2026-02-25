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
    doc_converter_form = DOCConvert()
    pdf_converter_form = PDFConvert()
    txt_converter_form = TXTConvert()
    csv_converter_form = CSVConvert()
    
    if pdf_converter_form.validate_on_submit():
        convert_pdf_ = PDF_CONVERT()
        user_upload = pdf_converter_form.file_doc.data
        
        # CONVERT PDF TO TXT & SEND BACK TO USER
        if pdf_converter_form.convert_to_txt.data:
            file_stream, file_name_title = convert_pdf_.PDF_to_TXT(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        
        elif pdf_converter_form.convert_to_doc.data:
            file_stream, file_name_title = convert_pdf_.PDF_to_DOC(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        
        elif pdf_converter_form.convert_to_csv.data:
            file_stream, file_name_title = convert_pdf_.PDF_to_CSV(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        
    elif txt_converter_form.validate_on_submit():
        user_upload = txt_converter_form.file_doc.data
        pass
    elif csv_converter_form.validate_on_submit():
        user_upload = csv_converter_form.file_doc.data
        pass
    
    return render_template("file.html", file_types=file_types, 
                           file_type=file_type, 
                           doc_converter_form=doc_converter_form,
                           pdf_converter_form=pdf_converter_form, 
                           txt_converter_form=txt_converter_form, 
                           csv_converter_form=csv_converter_form,)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return redirect('homepage')
