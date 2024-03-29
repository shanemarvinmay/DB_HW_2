#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys

def read_input(file):
    for line in file:
        # Split the line into words
        yield line.split('\t')

def parse_city(location):
    city = location[0]
    return city.strip().title()

def main():
    # Input comes from STDIN (standard input)
    rows = read_input(sys.stdin)
    for row in rows:
        conference = row[1]
        location = row[2].split(',')
        if len(location) > 1:
            city = parse_city(location)
            print(f'{conference}\t{city}')

if __name__ == "__main__":
    main()