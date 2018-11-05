""" 
Recursively walks down a directory, finding all PDFs, and collects their first
pages.
"""

import argparse
import os
import PyPDF2
import re

PDF_REGEX = r"pdf\Z"
OUTFILE = "out.pdf"

class Collector():
    def __init__(self, dir, out, match):
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
    args = parse_args()
    print(args)

    collector = Collector(args.dir, args.out, args.regex)
    collector.collect()
    collector.write()

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('dir', type=str, nargs='?', default=os.curdir)
    parser.add_argument('-o', '--out', type=str, default=OUTFILE)
    parser.add_argument('-r', '--regex', type=str, default=PDF_REGEX)
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()