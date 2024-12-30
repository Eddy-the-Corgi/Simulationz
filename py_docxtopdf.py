import subprocess
from PyPDF2 import PdfMerger

def docx_to_pdf(docx_path, pdf_path):
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', docx_path])

def concatenate_pdfs(pdf_paths, output_path):
    merger = PdfMerger()
    for pdf in pdf_paths:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

docx_files = ["pl1.docx", "pl2.docx", "pl3.docx"]
pdf_files = []

for docx in docx_files:
    pdf_file = docx.replace('.docx', '.pdf')
    docx_to_pdf(docx, pdf_file)
    pdf_files.append(pdf_file)

concatenate_pdfs(pdf_files, "output.pdf")