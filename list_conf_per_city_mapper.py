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

def parse_conference_acronym(conference):
    # Removing the year from the acronym.
    conference_parts = conference.split(' ')
    if conference_parts[-1].isnumeric():
        conference_parts.pop()
    conference = ''.join(conference_parts)
    # Make sure the acronym is upper case and without whitespace.
    return conference.strip().upper()


def main():
    # Input comes from STDIN (standard input)
    rows = read_input(sys.stdin)
    for row in rows:
        conference = row[0]
        location = row[2].split(',')
        if len(location) > 1:
            city = parse_city(location)
            conference = parse_conference_acronym(conference)
            print(f'{city}\t{conference}')

if __name__ == "__main__":
    main()