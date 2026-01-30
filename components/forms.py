from wtforms import FileField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed
'''Flask Forms For Application'''

# create a form for converting files in txt format
class TXTConvert(FlaskForm):
    '''a form for converting files in txt format'''
    file_doc = FileField("Upload TXT", validators=[
        FileRequired(),
        FileAllowed(['txt'], "Unsupported File")])
    
    convert_to_pdf = SubmitField("Convert To .pdf File")
    convert_to_csv = SubmitField("Convert To .csv File")
    convert_to_doc = SubmitField("Convert To .doc File")
    
# create a form for converting files in doc format
class DOCConvert(FlaskForm):
    '''a form for converting files in doc format'''
    file_doc = FileField("Upload DOC", validators=[
        FileRequired(),
        FileAllowed(['doc', 'docx'], "Unsupported File")])
    
    convert_to_pdf = SubmitField("Convert To .pdf File")
    convert_to_txt = SubmitField("Convert To .txt File")
    convert_to_csv = SubmitField("Convert To .csv File")

# create a form for converting files in pdf format
class PDFConvert(FlaskForm):
    '''a form for converting files in pdf format'''
    file_doc = FileField("Upload PDF", validators=[
        FileRequired(),
        FileAllowed(['pdf'], "Unsupported File")])
    
    convert_to_txt = SubmitField("Convert To .txt File")
    convert_to_csv = SubmitField("Convert To .csv File")
    convert_to_doc = SubmitField("Convert To .doc File")

# create a form for converting files in csv format
class CSVConvert(FlaskForm):
    '''a form for converting files in csv format'''
    file_doc = FileField("Upload CSV", validators=[
        FileRequired(),
        FileAllowed(['csv'], "Unsupported File")])
    
    convert_to_txt = SubmitField("Convert To .txt File")
    convert_to_doc = SubmitField("Convert To .doc File")
    convert_to_pdf = SubmitField("Convert To .pdf File")
       