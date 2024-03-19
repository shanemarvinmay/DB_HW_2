#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys

def read_input(file):
    for line in file:
        # Split the line into words
        yield line.split('\t')

def parse_city(location):
    # Extract the city and return it in title case.
    city = location[0]
    return city.strip().title()

def main():
    # Input comes from STDIN (standard input)
    rows = read_input(sys.stdin)
    for row in rows:
        # Split the location into parts.
        # Each part is either the country, state, city, or school.
        location = row[2].split(',')
        # Making sure the city was listed and not just the countr/state.
        if len(location) < 2:
            continue
        # Attempting to parse the year.
        try:
            year = int(row[3])
            city = parse_city(location)
            print(f'{year}\t{city}')
        except:
            continue

if __name__ == "__main__":
    main()