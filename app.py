from flask import Flask, render_template, redirect, send_file
from components.data import file_types
from components.forms import DOCConvertForm, PDFConvertForm, TXTConvertForm, CSVConvertForm
from components.functions import PDF_CONVERT, TXT_CONVERT, CSV_CONVERT, DOC_CONVERT
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.route('/homepage')
def homepage():
    return render_template("index.html")

@app.route("/convert/<file_type>", methods=['GET', 'POST'])
def convert(file_type):
    file_type = file_type.upper()
    user_upload = None
    doc_converter_form = DOCConvertForm()
    pdf_converter_form = PDFConvertForm()
    txt_converter_form = TXTConvertForm()
    csv_converter_form = CSVConvertForm()
    
    if pdf_converter_form.validate_on_submit():
        convert_pdf_ = PDF_CONVERT()
        user_upload = pdf_converter_form.file_doc.data
        
        # CONVERT PDF & SEND BACK TO USER
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
        convert_txt_ = TXT_CONVERT()
        user_upload = txt_converter_form.file_doc.data
        
        # CONVERT TEXT & SEND BACK TO USER
        if txt_converter_form.convert_to_pdf.data:
            file_stream, file_name_title = convert_txt_.TXT_to_PDF(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif txt_converter_form.convert_to_doc.data:
            file_stream, file_name_title = convert_txt_.TXT_to_DOC(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif txt_converter_form.convert_to_csv.data:
            file_stream, file_name_title = convert_txt_.TXT_to_CSV(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
    elif csv_converter_form.validate_on_submit():
        convert_csv_ = CSV_CONVERT()
        user_upload = csv_converter_form.file_doc.data
        
        # CONVERT CSV & SEND BACK TO USER
        if csv_converter_form.convert_to_pdf.data:
            file_stream, file_name_title = convert_csv_.CSV_to_PDF(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif csv_converter_form.convert_to_doc.data:
            file_stream, file_name_title = convert_csv_.CSV_to_DOC(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif csv_converter_form.convert_to_txt.data:
            file_stream, file_name_title = convert_csv_.CSV_to_TXT(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
    elif doc_converter_form.validate_on_submit():
        convert_doc_ = DOC_CONVERT()
        user_upload = doc_converter_form.file_doc.data
        
        if doc_converter_form.convert_to_pdf.data:
            file_stream, file_name_title = convert_doc_.DOC_to_PDF(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif doc_converter_form.convert_to_csv.data:
            file_stream, file_name_title = convert_doc_.DOC_to_CSV(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
        elif doc_converter_form.convert_to_txt.data:
            file_stream, file_name_title = convert_doc_.DOC_to_TXT(user_upload)
            return send_file(path_or_file=file_stream, as_attachment=True, download_name=file_name_title)
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
