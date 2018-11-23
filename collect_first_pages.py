""" 
Recursively walks down a directory, finding all PDFs, and collects their first
pages.
"""

import argparse
import os
import re
import subprocess
import pipes
import PyPDF2

PDF_REGEX = r"pdf\Z"
OUTFILE = "out.pdf"
QPDF_PATH = "./qpdf-8.2.1/bin/qpdf.exe"

class Collector():
    def __init__(self, dir, out, qpdf_path,  match):
        self.dir = dir
        self.regex = re.compile(match, re.IGNORECASE)
        self.outfile = out
        self.qpdf_path = qpdf_path
        self.pagecount = 0
        self.pdf = PyPDF2.PdfFileWriter()

    def collect(self):
        for dir, _, files in os.walk(self.dir):
            for file in files:
                if self.regex.search(file):
                    path = os.path.join(os.path.abspath(dir), file)
                    self.decrypt_in_place(path)
                    self.append_first_page(path)

    def decrypt_in_place(self, path):
        print(f"decrypting {path}")
        tmppath = path + ".tmp"
        cmd = [self.qpdf_path, "--decrypt", path, tmppath]
        subprocess.run(cmd, shell=True, check=True)
        os.remove(path)
        os.rename(tmppath, path)
    
    def append_first_page(self, path):
        print(f"adding page {self.pagecount + 1}")
        pdf = PyPDF2.PdfFileReader(path)
        firstpage = pdf.getPage(0)
        self.pdf.addPage(firstpage)
        self.pagecount += 1

    def write(self):
        if self.pagecount == 0:
            return
        with open(self.outfile, "wb") as outfile:
            self.pdf.write(outfile)

def main():
    args = parse_args()
    collector = Collector(
        os.path.abspath(args.dir), 
        os.path.abspath(args.out), 
        os.path.abspath(args.qpdf),
        args.regex)
    collector.collect()
    collector.write()
    print("done")


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('dir', type=str, nargs='?', default=os.curdir)
    parser.add_argument('-o', '--out', type=str, default=OUTFILE)
    parser.add_argument('-r', '--regex', type=str, default=PDF_REGEX)
    parser.add_argument('-q', '--qpdf', type=str, default=QPDF_PATH)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
