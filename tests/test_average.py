import pytest
import average


def test_average_sentence_length():
    with open('tests/test_doc.txt', 'r') as fp:
        testfile = fp.read()
    results = average.get(testfile)
    assert results['average'] == 17.25
    assert results['number_of_sentences'] == 4
    assert results['shortest'] == 16
    assert results['longest'] == 19
    assert results['stdev'] == 1.26
