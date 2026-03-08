from PyPDF2 import PdfReader #used for for exsisting pdf
from PyPDF2.errors import PdfReadError, FileNotDecryptedError
from werkzeug.utils import secure_filename
from fpdf import FPDF #used to create new pdf
import textcase
import io


# create function to extract text from PDF
class PDF_CONVERT():
    """
    Handles conversion from PDF to other text-based formats.
    """
    # PDF TO TXT
    def PDF_to_TXT(self, file_=str):
        """
        Extracts text from a PDF file and returns it as a TXT file stream.
        """
        try:
            file_reader = PdfReader(file_)
            page_num = len(file_reader.pages)
            extracted_text = ""
            title = file_reader.metadata.title if file_reader.metadata and file_reader.metadata.title else file_.filename.rsplit('.', 1)[0]
            safe_name = secure_filename(textcase.snake(title.strip()))
            file_name_title = safe_name + '.txt'
            for num in range(page_num):
                text_ = file_reader.pages[num]
                extracted_text += text_.extract_text()

            # Use in-memory file
            file_stream = io.BytesIO()
            file_stream.write(extracted_text.encode('utf-8'))
            file_stream.seek(0)
            return file_stream, file_name_title
        except PdfReadError:
            error_message = "Error: The PDF file is corrupted or invalid."
            return None, error_message
        except FileNotDecryptedError:
            error_message = "Error: PDF document not decrypted"
            return None, error_message
        except Exception as e:
            error_message = f"Error: {e}"
            return None, error_message
    
    # PDF TO DOC
    def PDF_to_DOC(self, file_=str):
        """
        Extracts text from a PDF file and returns it as a DOC file stream.
        """
        try:
            file_reader = PdfReader(file_)
            page_num = len(file_reader.pages)
            extracted_text = ""
            title = file_reader.metadata.title if file_reader.metadata and file_reader.metadata.title else file_.filename.rsplit('.', 1)[0]
            safe_name = secure_filename(textcase.snake(title.strip()))
            file_name_title = safe_name + '.doc'
            for num in range(page_num):
                text_ = file_reader.pages[num]
                extracted_text += text_.extract_text()

            # Use in-memory file
            file_stream = io.BytesIO()
            file_stream.write(extracted_text.encode('utf-8'))
            file_stream.seek(0)
            return file_stream, file_name_title
        except PdfReadError:
            error_message = "Error: The PDF file is corrupted or invalid."
            return None, error_message
        except FileNotDecryptedError:
            error_message = "Error: PDF document not decrypted"
            return None, error_message
        except Exception as e:
            error_message = f"Error: {e}"
            return None, error_message

    def PDF_to_CSV(self, file_=str):
        """
        Extracts text from a PDF file and returns it as a CSV file stream.
        """
        try:
            file_reader = PdfReader(file_)
            page_num = len(file_reader.pages)
            extracted_text = ""
            title = file_reader.metadata.title if file_reader.metadata and file_reader.metadata.title else file_.filename.rsplit('.', 1)[0]
            safe_name = secure_filename(textcase.snake(title.strip()))
            file_name_title = safe_name + '.csv'
            for num in range(page_num):
                text_ = file_reader.pages[num]
                extracted_text += text_.extract_text()
            
            # in-memory file logic for security 
            file_stream = io.BytesIO()
            file_stream.write(extracted_text.encode('utf-8'))
            file_stream.seek(0)
            return file_stream, file_name_title
        except PdfReadError:
            error_message = "Error: The PDF file is corrupted or invalid."
            return None, error_message
        except FileNotDecryptedError:
            error_message = "Error: PDF document not decrypted"
            return None, error_message
        except Exception as e:
            error_message = f"Error: {e}"
            return None, error_message
  
class TXT_CONVERT(): 
    """
    Handles conversion from TXT to other formats.
    """
             
    def TXT_to_PDF(self, file_=str):
        """
        Converts a TXT file to a PDF file stream.
        """
        #get title from filename
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.pdf'
        
        # 2. Read text from the FileStorage object
        # Reset stream pointer to ensure we read from the beginning
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        # For Reference, this is how to write to pdf using FPDF
        # Create the PDF object
        pdf_object = FPDF()
        pdf_object.add_page()
        
        # Set font (required before writing)
        font_path = "static/fonts/DejaVuSans.ttf"
        pdf_object.add_font("DejaVu", style="", fname=font_path)
        pdf_object.set_font("DejaVu", size=12)
        
        # Write text using multi_cell for automatic line wrapping
        # 0 = full width of a page; 10 = line height
        pdf_object.multi_cell(0, 10, text=str(extracted_text))
        
        # Output to a string/bytes and wrap in BytesIO
        # Adding dest='S' returns the document as a string (latin-1 encoded in original fpdf)
        pdf_output = pdf_object.output(dest='S')
        if isinstance(pdf_output, str):
            pdf_output = pdf_output.encode('latin-1')
            
        # use in-memory file
        file_stream = io.BytesIO(pdf_output)
        file_stream.seek(0)
        
        return file_stream, file_name_title
        
    def TXT_to_DOC(self, file_=str):
        """
        Converts a TXT file to a DOC file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.doc'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
    
    def TXT_to_CSV(self, file_=str):
        """
        Converts a TXT file to a CSV file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.csv'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
 
class CSV_CONVERT():
    """
    Handles conversion from CSV to other formats.
    """
    def CSV_to_PDF(self, file_):
        """
        Converts a CSV file to a PDF file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.pdf'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        pdf_object = FPDF()
        pdf_object.add_page()
        
        font_path = "static/fonts/DejaVuSans.ttf"
        pdf_object.add_font("DejaVu", style="", fname=font_path)
        pdf_object.set_font("DejaVu", size=12)
        
        pdf_object.multi_cell(0, 10, text=str(extracted_text))
        
        pdf_output = pdf_object.output(dest='S')
        if isinstance(pdf_output, str):
            pdf_output = pdf_output.encode('latin-1')
            
        # use in-memory file
        file_stream = io.BytesIO(pdf_output)
        file_stream.seek(0)
        
        return file_stream, file_name_title
    
    def CSV_to_DOC(self, file_=str):
        """
        Converts a CSV file to a DOC file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.doc'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
    
    def CSV_to_TXT(self, file_=str):
        """
        Converts a CSV file to a TXT file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.txt'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
    
class DOC_CONVERT():
    """
    Handles conversion from DOC to other formats.
    """
    
    def DOC_to_PDF(self, file_):
        """
        Converts a DOC file to a PDF file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.doc'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        pdf_object = FPDF()
        pdf_object.add_page()
        
        font_path = "static/fonts/DejaVuSans.ttf"
        pdf_object.add_font("DejaVu", style="", fname=font_path)
        pdf_object.set_font("DejaVu", size=12)
        
        pdf_object.multi_cell(0, 10, text=str(extracted_text))
        
        pdf_output = pdf_object.output(dest='S')
        if isinstance(pdf_output, str):
            pdf_output = pdf_output.encode('latin-1')
            
        # use in-memory file
        file_stream = io.BytesIO(pdf_output)
        file_stream.seek(0)
        
        return file_stream, file_name_title
        
    def DOC_to_TXT(self, file_=str):
        """
        Converts a DOC file to a TXT file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.txt'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
    
    def DOC_to_CSV(self, file_=str):
        """
        Converts a DOC file to a CSV file stream.
        """
        title = file_.filename.rsplit('.', 1)[0]
        safe_name = secure_filename(textcase.snake(title.strip()))
        file_name_title = safe_name + '.csv'
        
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title