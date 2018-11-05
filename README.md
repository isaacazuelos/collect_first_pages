# Collect First Pages

Collect the first page of all PDFs in a directory into a new PDF.

This isn't particularity general, but it's useful at work.
For a more general tool, see [`pdfcat`][1]

[1]: https://pythonhosted.org/PyPDF2/Easy%20Concatenation%20Script.html

## Requirements and Installation

You'll need [Python 3][python], with the [`PyPDF2`][py2pdf] module installed.

[python]: https://python.org
[py2pdf]: https://pythonhosted.org/PyPDF2/

You can install `PyPDF2` with `pip install pypdf2`.

Clone the repository and use the `collect_first_pages.py` script as-is.

## Usage

Drag the file to the directory and double click it (if it's set to open with
python.) You can also run it from a command line, with extra arguments.

> `usage: collect_first_pages.py [-h] [-o OUT] [-r REGEX] [dir]`

- `--help` prints a help message.
- `dir` is the directory to traverse looking for pdfs.
- `--out` is the file path to write to.
- `--regex` is a [regular expression][regex] to use to specify which files to
  use. The default is `\.pdf\Z`. These are in Python's regex syntax.

[regex]: https://www.digitalocean.com/community/tutorials/an-introduction-to-regular-expressions

## Tests

I don't want to distribute example PDFs for testing, so you'll need to just run
it yourself and test.

You can get some good test files from
[uwaterloo](https://uwaterloo.ca/onbase/help/sample-pdf-documents).

## License

This project is under the [MIT license](https://opensource.org/licenses/MIT).

See the included `LICENSE` file.