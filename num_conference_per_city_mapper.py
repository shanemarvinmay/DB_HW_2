#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys

def read_input(file):
    for line in file:
        # Split the line into words
        yield line.split('\t')

def main():
    # Input comes from STDIN (standard input)
    rows = read_input(sys.stdin)
    for row in rows:
        location = row[2].split(',')
        # If the location length is greater than 1, then a city was most likely specified.
        if len(location) > 1:
            city = location[0]
            city = city.strip().title()
            print(f'{city}\t1')

if __name__ == "__main__":
    main()