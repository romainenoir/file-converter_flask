from PyPDF2 import PdfReader
import textcase

# create function to extract text from PDF

class PDF_CONVERT():
    """A utility class for converting PDF files to different document formats.
    
    This class provides methods to extract text from PDF files and convert them
    to various output formats such as TXT and DOC files. The converted files are
    named based on the PDF's metadata title.
    
    Methods:
        PDF_to_TXT(file_): Converts a PDF file to plain text format (.txt)
        PDF_to_DOC(file_): Converts a PDF file to document format (.doc)
    """
    
    # PDF TO TXT
    def PDF_to_TXT(self, file_=str):
        """ PDF TO TXT
            (file_ = name of the file)"""
        file_reader = PdfReader(file_)
        page_num = file_reader._get_num_pages()
        extracted_text = ""
        file_name_title = textcase.snake(file_reader.metadata.title.strip()) + '.txt'
        for num in range(page_num):
            text_ = file_reader.pages[num]
            extracted_text += text_.extract_text()
        
        with open(file_name_title, 'w') as file:
            file.write(extracted_text)
    
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
        file_name_title = textcase.snake(file_reader.metadata.title.strip()) + '.doc'
        for num in range(page_num):
            text_ = file_reader.pages[num]
            extracted_text += text_.extract_text()
        
        with open(file_name_title, 'w') as file:
            file.write(extracted_text)

