from wtforms import FileField, SubmitField
from flask_wtf import FlaskForm

# create a form for converting files in txt format
class TXTConvert(FlaskForm):
    '''a form for converting files in txt format'''
    file_doc = FileField("Upload TXT")
    
    convert_to_pdf = SubmitField("Convert To .pdf File")
    convert_to_csv = SubmitField("Convert To .csv File")
    convert_to_doc = SubmitField("Convert To .doc File")
    
# create a form for converting files in doc format
class DOCConvert(FlaskForm):
    '''a form for converting files in doc format'''
    file_doc = FileField("Upload DOC")
    
    convert_to_pdf = SubmitField("Convert To .pdf File")
    convert_to_txt = SubmitField("Convert To .txt File")
    convert_to_csv = SubmitField("Convert To .csv File")

# create a form for converting files in pdf format
class PDFConvert(FlaskForm):
    '''a form for converting files in pdf format'''
    file_doc = FileField("Upload PDF")
    
    convert_to_txt = SubmitField("Convert To .txt File")
    convert_to_csv = SubmitField("Convert To .csv File")
    convert_to_doc = SubmitField("Convert To .doc File")

# create a form for converting files in csv format
class CSVConvert(FlaskForm):
    '''a form for converting files in csv format'''
    file_doc = FileField("Upload PDF")
    
    convert_to_txt = SubmitField("Convert To .txt File")
    convert_to_doc = SubmitField("Convert To .doc File")
    convert_to_pdf = SubmitField("Convert To .pdf File")
       