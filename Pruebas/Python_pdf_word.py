from pdf2docx import Converter

def convert_pdf_word (pdf_path, docx_path):
    try:
        cv = Converter(pdf_path)
        cv.convert (docx_path, start = 0, end = None)
        cv.close()
    except Exception as e:
        print (f'Error: {e}')

"""pdf_path = 'C:/Personal/FCFM/POI/2023_02_FE_CL_POI.pdf'
docx_path = 'C:/Personal/FCFM/POI/2023_02_FE_CL_POI2.docx'
"""
pdf_path = 'C:/Codigos/PY_ECOMM/aws_codewhisper_python_ecommerce.pdf'
docx_path = 'C:/Codigos/PY_ECOMM/aws_codewhisper_python_ecommerce.docx'

convert_pdf_word (pdf_path, docx_path)