from PyPDF2 import PdfReader
import textcase

# create function to extract text from PDF
def PDF_to_TXT(file_=str):
    """_summary_
        CONVERTS PDFs TO TXTs
    Args:
        file_ (_type_, optional): name of file. Defaults to str.
    """
    file_reader = PdfReader(file_)
    page_num = file_reader._get_num_pages()
    extracted_text = ""
    file_name_title = textcase.snake(file_reader.metadata.title) + '.txt'
    file_name_title.strip()
    for num in range(page_num):
        text_ = file_reader.pages[num]
        extracted_text += text_.extract_text()
    
    with open(file_name_title, 'w') as file:
        file.write(extracted_text)
        

    
PDF_Extract("pdf_dummi.pdf")