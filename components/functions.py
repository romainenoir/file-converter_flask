from PyPDF2 import PdfReader

# create function to extract text from PDF
def PDF_Extract(file_=str):
    file_reader = PdfReader(file_)
    page_num = file_reader._get_num_pages()
    for num in range(page_num):
        text_ = file_reader.pages[num]
        return text_.extract_text()
    
converted_file = PDF_Extract("pdf_dummi.pdf")
print(converted_file)