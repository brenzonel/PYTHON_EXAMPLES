from PyPDF2 import PdfFileReader

def pdf_info(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    
    text = f"""
    Information about {pdf_path}: 

    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of pages: {number_of_pages}
    """
    print(text)

    return info

if __name__ == '__main__':
    path = 'DOC-20170504-WA0003.pdf'
    pdf_info(path)