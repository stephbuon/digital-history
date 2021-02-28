import spacy
import pandas as pd
from os import cpu_count
import argparse

from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")
DEFAULT_CPU_COUNT = 3


class Config:
    """
    Keeps track of configuration options that we can pass around to other processes.
    """
    CHUNK_SIZE = 2**15
    CPU_CORES = 3
    INPUT_FILE = ''
    OUTPUT_FILE = ''


def parse_config():
    """
    Parses and validates command line arguments.
    :return: Config object filled with the corresponding configuration for the specified CL arguments.
    """
    config = Config()
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input data file')
    parser.add_argument('output_file', help='output data file')
    parser.add_argument('--cores', default=DEFAULT_CPU_COUNT, type=int, help='Number of cores to use.')
    args = parser.parse_args()

    config.INPUT_FILE = args.input_file
    print('INPUT_FILE:', config.INPUT_FILE)

    config.OUTPUT_FILE = args.output_file
    print('OUTPUT_FILE:', config.OUTPUT_FILE)

    config.CPU_CORES = args.cores
    if config.CPU_CORES < 0 or config.CPU_CORES > cpu_count():
        raise ValueError('Invalid core number specified.')

    print('CPU_CORES:', config.CPU_CORES)
    return config


if __name__ == '__main__':
    conf = parse_config()
    df = pd.read_csv(conf.INPUT_FILE, usecols=['sentence_id', 'text'])

    if spacy.__version__[0] == '3':
        # Spacy v3 saved all attributes by default.
        doc_bin = DocBin(store_user_data=True)
    else:
        doc_bin = DocBin(["LEMMA", "ENT_TYPE", "POS", "DEP"], store_user_data=True)

    for i, doc in enumerate(nlp.pipe(df['text'], n_process=conf.CPU_CORES)):
        if doc.is_parsed:
            doc.user_data['sentence_id'] = df.iloc[i, 0]
            doc_bin.add(doc)

    print('Writing file...')
    bytes_data = doc_bin.to_bytes()
    with open(conf.OUTPUT_FILE, 'wb+') as f:
        f.write(bytes_data)
    print('Exiting...')
