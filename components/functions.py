from PyPDF2 import PdfReader, PdfWriter #used for for exsisting pdfs
from fpdf import FPDF #used to create new pdf
import textcase
import io


# create function to extract text from PDF
class PDF_CONVERT():
    """A utility class for converting PDF files to different document formats.
    
    This class provides methods to extract text from PDF files and convert them
    to various output formats such as TXT and DOC files. The converted files are
    named based on the PDF's metadata title.
    
    Methods:
        PDF_to_TXT(file_): Converts a PDF file to plain text format (.txt)
        PDF_to_DOC(file_): Converts a PDF file to document format (.doc)
        PDF_to_CSV(file_): Converts a PDF file to csv format (.doc)
    """
    
    # PDF TO TXT
    def PDF_to_TXT(self, file_=str):
        """ PDF TO TXT
            (file_ = name of the file)"""
        file_reader = PdfReader(file_)
        page_num = file_reader._get_num_pages()
        extracted_text = ""
        title = file_reader.metadata.title if file_reader.metadata and file_reader.metadata.title else file_.filename.rsplit('.', 1)[0]
        file_name_title = textcase.snake(title.strip()) + '.txt'
        for num in range(page_num):
            text_ = file_reader.pages[num]
            extracted_text += text_.extract_text()

        # Use in-memory file
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
    
    # PDF TO DOC
    def PDF_to_DOC(self, file_=str):
        """_summary_
            CONVERTS PDFs TO DOCs
        Args:
            file_ (_type_, optional): name of file. Defaults to str.
        """
        file_reader = PdfReader(file_)
        page_num = file_reader._get_num_pages()
        extracted_text = ""
        title = file_reader.metadata.title if file_reader.metadata and file_reader.metadata.title else file_.filename.rsplit('.', 1)[0]
        file_name_title = textcase.snake(title.strip()) + '.doc'
        for num in range(page_num):
            text_ = file_reader.pages[num]
            extracted_text += text_.extract_text()

        # Use in-memory file
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title

    def PDF_to_CSV(self, file_=str):
        """_summary_
            CONVERTS PDFs TO CSVs
        Args:
            file_ (_type_, optional): name of file. Defaults to str.
        """
        file_reader = PdfReader(file_)
        page_num = file_reader._get_num_pages()
        extracted_text = ""
        title = file_reader.metadata.title if file_reader.metadata and file_reader.metadata.title else file_.filename.rsplit('.', 1)[0]
        file_name_title = textcase.snake(title.strip()) + '.csv'
        for num in range(page_num):
            text_ = file_reader.pages[num]
            extracted_text += text_.extract_text()
        
        # in-memory file logic for security 
        file_stream = io.BytesIO()
        file_stream.write(extracted_text.encode('utf-8'))
        file_stream.seek(0)
        return file_stream, file_name_title
  
class TXT_CONVERT():
    """A utility class for converting TXT files to different document formats.

        This class provides methods to extract text from TXT files and convert them
        to various output formats such as PDF, DOC & CSV files. The converted files are
        named based on the TXT's metadata title.
        
        Methods:
            PDF_to_TXT(file_): Converts a PDF file to plain text format (.txt)
            PDF_to_DOC(file_): Converts a PDF file to document format (.doc)
            PDF_to_CSV(file_): Converts a PDF file to csv format (.doc)
    """  
             
    def TXT_to_PDF(self, file_=str):
        """_summary_
            Converts .txt into .pdf
        Args:
            file_ (_type_, optional): _description_. Defaults to str.
        Returns:
            _type_: _description_
        """
        #get title from filename
        title = file_.filename.rsplit('.', 1)[0]
        file_name_title =  textcase.snake(title.strip()) + '.pdf'
        
        # 2. Read text from the FileStorage object
        # Reset stream pointer to ensure we read from the beginning
        file_.seek(0)
        extracted_text = file_.read().decode('utf-8')
        
        # For Reference, this is how to write to pdf using FPDF
        # Create the PDF object
        pdf_object = FPDF()
        pdf_object.add_page()
        
        # Set font (required before writing)
        pdf_object.set_font("Arial", size=12)
        
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
        