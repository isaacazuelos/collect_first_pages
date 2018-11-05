""" 
Recursively walks down a directory, finding all PDFs, and collects their first
pages.

This isn't particularity general, but it's useful at work.
For a more general tool, see pdfcat[1]

[1]: https://pythonhosted.org/PyPDF2/Easy%20Concatenation%20Script.html
"""

import os
import PyPDF2

LOGFILE_PATH = "error-log.txt"
PDF_EXTENSION = ".pdf"

def log(s):
    with open(LOGFILE_PATH, 'a') as logfile:
        logfile.write(s + "\n")

def append_first_page(writer, path):
    print("appending:", path)
    pdf = PyPDF2.PdfFileReader(path)
    firstpage = pdf.getPage(0)
    writer.addPage(firstpage)

def has_pdf_ext(path):
    _, ext = os.path.splitext(path)
    return ext.lower() == PDF_EXTENSION

def first_pages_of_pdfs_recursively(dir=os.curdir):
    pdf = PyPDF2.PdfFileWriter()
    for dir, _, files in os.walk(dir):
        for file in files:
            if has_pdf_ext(file):
                append_first_page(pdf, file)
    return pdf

def write_pdf(pdf):
    with open("example.pdf", "wb") as outfile:
        pdf.write(outfile)

def main():
    try:
        pdf = first_pages_of_pdfs_recursively()
        write_pdf(pdf)
    except Exception as e:
        log("error: {}".format(e))

if __name__ == "__main__":
    main()