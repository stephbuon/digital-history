import sys

if sys.version_info.major < 3:
    exit('Python 3 required.')

try:
    import fitz
except ModuleNotFoundError as e:
    print('PyMuPDF is missing. Install using `pip install pymupdf`')
    raise e

import pandas as pd

import datetime
import os
from typing import Optional


def extract_text(filepath: str) -> str:
    pdf = fitz.Document(filepath)

    texts = []

    for i in range(pdf.pageCount):
        page = pdf[i]
        textPage = page.getTextPage()
        rawText = textPage.extractText()
        rawText = rawText.replace('\n', ' ').replace('\t', ' ')
        texts.append(rawText)

    return ' '.join(texts)


def parse_date(name: str) -> Optional[datetime.datetime]:
    formats = ['%Y%m%d', '%m%d%yMin', 'cc%m%d%y']

    for format in formats:
        try:
            return datetime.datetime.strptime(name, format)
        except ValueError:
            continue


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Extracts text from all PDFs inside the input directory and exports into a Pipe-seperated CSV file.'
    )
    parser.add_argument('-d', required=True, metavar='input_directory', help='Target input directory containing PDF files to process')
    parser.add_argument('-o', required=True, metavar='output_file', help='Output filename')

    args = parser.parse_args()

    directory = args.d

    rows = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for fn in filenames:
            name, extension = fn.rsplit('.', maxsplit=1)
            if extension != 'pdf':
                continue

            date = parse_date(name)

            if date is None:
                print(f'Skipping {fn}: could not parse date from filename')
                continue

            filepath = os.path.join(dirpath, fn)

            text = extract_text(filepath)

            rows.append((name, date.strftime('%Y-%m-%d'), text))

            print(f'Parsed {fn}')

    print(f'{len(rows)} files parsed. Exporting to {args.o}...')

    council_df = pd.DataFrame(rows, columns=['Filename', 'Date', 'Text'])
    council_df.index.name = 'index'
    council_df.to_csv(args.o, sep='|')
