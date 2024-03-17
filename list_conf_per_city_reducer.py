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
    #   city - string containing the city
    #   group - iterator yielding all conferences
    for city, group in groupby(data, itemgetter(0)):
        try:
            conferences = [conference for _, conference in group]
            print(f"{city}\t{', '.join(conferences)}")
        except:
            # An error occured parsing the city and conferences.
            pass
        
if __name__ == "__main__":
    main()