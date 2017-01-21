#!/usr/bin/env python
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import statistics
import json


def get(text):
    """
    For a given document, return the average sentence length.
    """
    sentence_list = sent_tokenize(text.strip())
    word_list = [_remove_punctuation_and_tokenize(words) for words in sentence_list]
    length_list = [len(word) for word in word_list]
    return {
        "average": float(format(statistics.mean(length_list), '.2f')),
        "number_of_sentences": len(sentence_list),
        "longest": max(length_list),
        "shortest": min(length_list),
        "stdev": float(format(statistics.stdev(length_list), '.2f')),
    }

def _remove_punctuation_and_tokenize(sentence):
    """
    For a given sentence, remove the punctuation and return a tokened list of words.
    """
    return word_tokenize(sentence.translate(str.maketrans({a: None for a in string.punctuation})))

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Get average sentence length from a file.')
    parser.add_argument('filename', help='filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    results = get(args.filename.read())
    sys.stdout.write(json.dumps(results))
