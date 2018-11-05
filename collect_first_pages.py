""" 
Recursively walks down a directory, finding all PDFs, and collects their first
pages.
"""

import os
import re
import PyPDF2

LOGFILE_PATH = "error-log.txt"
PDF_REGEX = r"pdf\Z"
OUTFILE = "out.pdf"

def log(s):
    """ Add a string to the bottom of LOGFILE_PATH """
    with open(LOGFILE_PATH, 'a') as logfile:
        logfile.write(s + "\n")

class Collector():
    def __init__(self, dir=os.curdir, out="out.pdf", match=PDF_REGEX):
        self.pagecount = 0
        self.dir = dir
        self.regex = re.compile(match, re.IGNORECASE)
        self.outfile = out
        self.writer = PyPDF2.PdfFileWriter()

    def append_first_page(self, path):
        pdf = PyPDF2.PdfFileReader(path)
        firstpage = pdf.getPage(0)
        self.writer.addPage(firstpage)
        self.pagecount += 1

    def collect(self):
        for dir, _, files in os.walk(self.dir):
            for file in files:
                if self.regex.search(file):
                    path = os.path.join(dir, file)
                    self.append_first_page(path)

    def write(self):
        if self.pagecount == 0:
            return
        with open(self.outfile, "wb") as outfile:
            self.writer.write(outfile)

def main():
    try:
        collector = Collector()
        collector.collect()
        collector.write()
    except Exception as e:
        log("error: {}".format(e))

if __name__ == "__main__":
    main()