from pdf2docx import Converter

def convert_pdf_word (pdf_path, docx_path):
    try:
        cv = Converter(pdf_path)
        cv.convert (docx_path, start = 0, end = None)
        cv.close()
    except Exception as e:
        print (f'Error: {e}')

"""pdf_path = 'C:CFM/POI/doc.pdf'
docx_path = 'C:/POI/doc.docx'
"""
pdf_path = 'C:/python_ecommerce.pdf'
docx_path = 'C:/python_ecommerce.docx'

convert_pdf_word (pdf_path, docx_path)