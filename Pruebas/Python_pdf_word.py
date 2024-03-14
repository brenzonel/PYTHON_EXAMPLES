from pdf2docx import Converter

def convert_pdf_word (pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert (docx_path, start = 0, end = None)
    cv.close()

"""pdf_path = 'C:/Personal/FCFM/POI/2023_02_FE_CL_POI.pdf'
docx_path = 'C:/Personal/FCFM/POI/2023_02_FE_CL_POI2.docx'
"""
pdf_path = 'C:/Personal/FCFM/BD Multimedia/AGO_DEC_2023/Forma de Evaluacion/FE BDMM-AgoDic2023 (052).pdf'
docx_path = 'C:/Personal/FCFM/BD Multimedia/AGO_DEC_2023/Forma de Evaluacion/FE BDMM-AgoDic2023 (052).docx'

convert_pdf_word (pdf_path, docx_path)