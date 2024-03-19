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
    # read_mapper_output creates an iterator that returns consecutive keys and their group:
    #   conference - string containing the city
    #   group - iterator yielding all cities
    for conference, group in groupby(data, itemgetter(0)):
        try:
            cities = [city for _, city in group]
            unique_cities = set(cities)
            print(f"{conference}\t{', '.join(list(unique_cities))}")
        except:
            # An error occured parsing the city and conferences.
            pass
        
if __name__ == "__main__":
    main()