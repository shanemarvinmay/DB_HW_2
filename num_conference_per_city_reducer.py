#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        line = line.strip()
        yield line.split('\t')

def main():
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin)
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for city, group in groupby(data, itemgetter(0)):
        try:
            total = sum(int(count) for _, count in group)
            print(f"{city}\t{total}")
        except ValueError:
            # count was not a number, so silently discard this item
            pass
        # for city, count in group:
        #     print(f"{city}\t{i}")
        # try:
        #     total = sum(int(count) for _, count in group)
        #     print(f'{city}\t{total}')
        

if __name__ == "__main__":
    main()