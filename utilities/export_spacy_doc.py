import csv
import multiprocessing as mp
import time

import numpy as np
from queue import Empty
import spacy
import pandas as pd
from os import cpu_count
from os import environ
import argparse

nlp = spacy.load("en_core_web_sm")


class Config:
    """
    Keeps track of configuration options that we can pass around to other processes.
    """
    CHUNK_SIZE = 2**15
    CPU_CORES = 3
    USE_TOKENS = False
    USE_ENTITIES = False
    INPUT_FILE = ''

    if environ.get('SCRATCH'):
        ENTITIES_OUTFILE = environ.get('SCRATCH') + '/hansard_entities.csv'
        TOKENS_OUTFILE = environ.get('SCRATCH') + '/hansard_tokens.csv'
    else:
        ENTITIES_OUTFILE = 'hansard_entities.csv'
        TOKENS_OUTFILE = 'hansard_tokens.csv'


DEFAULT_CPU_COUNT = 3


def parse_config():
    """
    Parses and validates command line arguments.
    :return: Config object filled with the corresponding configuration for the specified CL arguments.
    """
    config = Config()
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input data file')
    parser.add_argument('--cores', default=DEFAULT_CPU_COUNT, type=int, help='Number of cores to use.')
    parser.add_argument('--export-tokens', action='store_true',
                        help='Whether to export tokenized words with lemmatization and spaCy POS tagging.')
    parser.add_argument('--export-entities', action='store_true',
                        help='Whether to export entries from the spaCy entity tagger.')
    args = parser.parse_args()

    config.INPUT_FILE = args.input_file
    print('INPUT_FILE:', config.INPUT_FILE)

    config.CPU_CORES = args.cores
    if config.CPU_CORES < 0 or config.CPU_CORES > cpu_count():
        raise ValueError('Invalid core number specified.')

    print('CPU_CORES:', config.CPU_CORES)

    config.USE_TOKENS = args.export_tokens
    config.USE_ENTITIES = args.export_entities

    print('USE_TOKENS:', config.USE_TOKENS)
    print('USE_ENTITIES:', config.USE_ENTITIES)
    return config


def worker_function(in_q: mp.Queue, out_q: mp.Queue, config: Config):
    """
    This function will run for N - 1 cores, awaiting chunks from the in_q. Stops once
    a None object is found in the in_q.

    :param in_q: a multiprocessing.Queue containing dataframe chunks to parse.
    :param out_q: a multiprocessing.Queue containing a tuple of (words, entities) where
    words is a list of rows of (sentence_id, text, lemma, part of speech tag),
    and entities is a list of rows of (sentence_id, text, entity label)
    :param config: configuration passed in by main process
    :return:
    """
    use_tokens, use_entities = config.USE_TOKENS, config.USE_ENTITIES

    while True:
        try:
            chunk: pd.DataFrame = in_q.get(block=True)
        except Empty:
            continue
        else:
            if chunk is None:
                # This is our signal that we are done here. Every other worker thread will get a similar signal.
                return

            words = []
            entities = []

            i = 0

            for doc in nlp.pipe(chunk['text']):
                if doc.is_parsed:
                    if use_tokens:
                        for n in doc:
                            words.append([chunk.iloc[i, 0], n.text, n.lemma_, n.pos_])
                    if use_entities:
                        for ent in doc.ents:
                            entities.append([chunk.iloc[i, 0], ent.text, ent.label_])

                i += 1

            out_q.put((words, entities))


def export(output_queue, config: Config):
    """
    This function will run in a single process, awaiting output from the worker processes.
    Will write to file as rows are received.
    
    :param output_queue: a multiprocessing.Queue containing a tuple of (words, entities) where
    words is a list of rows of (sentence_id, text, lemma, part of speech tag),
    and entities is a list of rows of (sentence_id, text, entity label)
    :param config: configuration passed in by main process
    :return:
    """
    use_tokens, use_entities = config.USE_TOKENS, config.USE_ENTITIES
    tokens_file, entities_file = config.TOKENS_OUTFILE, config.ENTITIES_OUTFILE

    if use_tokens:
        print(f'TOKENS_OUTFILE: {tokens_file}')
        tokens_outfile = open(tokens_file, 'w+', newline='', encoding='utf-8')
        tokens_wr = csv.writer(tokens_outfile, delimiter='|')
        tokens_wr.writerow(['sentence_id', 'text', 'lemma', 'pos'])
    else:
        tokens_outfile = None
        tokens_wr = None

    if use_entities:
        print(f'ENTITIES_OUTFILE: {entities_file}')
        entities_outfile = open(entities_file, 'w+', newline='', encoding='utf-8')
        entities_wr = csv.writer(entities_outfile, delimiter='|')
        entities_wr.writerow(['sentence_id', 'text', 'entity_label'])
    else:
        entities_outfile = None
        entities_wr = None

    n = 0

    t0 = time.time()

    while True:
        entry = output_queue.get(block=True)
        if entry is None:
            print(f'Finished all chunks. Total elapsed: {time.time() - t0:.2f} seconds')
            break
        else:
            n += 1

            tokens, entities = entry

            if use_tokens:
                for token in tokens:
                    tokens_wr.writerow(token)

            if use_entities:
                for entity in entities:
                    entities_wr.writerow(entity)

            print(f'elapsed: {(time.time() - t0) / 60:.2f} minutes | chunk count: {n}')

    print('Closing files...')
    if use_tokens:
        tokens_outfile.close()
    if use_entities:
        entities_outfile.close()


if __name__ == '__main__':
    conf = parse_config()

    in_q = mp.Queue()
    out_q = mp.Queue()

    # Reserve a core for the export process.
    process_args = (in_q, out_q, conf)
    processes = [mp.Process(target=worker_function, args=process_args) for _ in range(conf.CPU_CORES - 1)]
    for p in processes:
        p.start()

    export_process = mp.Process(target=export, args=(out_q, conf))
    export_process.start()

    num_chunks = 0
    for chunk in pd.read_csv(conf.INPUT_FILE,
                             usecols=['sentence_id', 'text'], chunksize=conf.CHUNK_SIZE):  # type: pd.DataFrame
        in_q.put(chunk)
        num_chunks += 1

    print(f'Queued {num_chunks} chunks with size {conf.CHUNK_SIZE}.')

    for _ in range(len(processes)):
        # Signals to process that no more entries will be added.
        in_q.put(None)

    for process in processes:
        process.join()

    # Tell export process to finish.
    out_q.put(None)

    print('waiting on export...')
    export_process.join()

    print('Exiting...')
