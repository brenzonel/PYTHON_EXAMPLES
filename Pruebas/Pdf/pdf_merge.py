import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    # List of PDF files to merge
    pdf_files = [
        'file1.pdf',
        'file2.pdf',
        'file3.pdf'
    ]

    # Output path for the merged PDF
    output_pdf = 'merged_output.pdf'

    # Merge the PDFs
    merge_pdfs(pdf_files, output_pdf)

    print(f"Merged PDF saved as {output_pdf}")