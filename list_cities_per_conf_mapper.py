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

def parse_conference_name(conference):
    # Removing part with parathensis that contain the acronym and year.
    parts = conference.split('(')
    i = 0
    while i < len(parts):
        if ')' in parts[i]:
            del parts[i]
        else:
            i += 1
    conference = ''.join(parts)
    # Removing any numeric parts like '12th' and year.
    conference_parts = conference.split(' ')
    i = 0
    while i < len(conference_parts):
        contains_number = any([char for char in conference_parts[i] if char.isdigit()])
        if len(conference_parts[i]) < 1 or contains_number:
            del conference_parts[i]
        else:
            i += 1
    conference = ' '.join(conference_parts)
    # Make sure the acronym is title case and without whitespace.
    return conference.strip().title()

def main():
    # Input comes from STDIN (standard input)
    rows = read_input(sys.stdin)
    for row in rows:
        acronym = row[0]
        conference = row[1]
        location = row[2].split(',')
        if len(location) > 1:
            city = parse_city(location)
            conference = parse_conference_name(conference)
            acronym = parse_conference_acronym(acronym)
            print(f'{conference}\t{city}')

if __name__ == "__main__":
    main()