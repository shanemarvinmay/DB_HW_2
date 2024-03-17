import pandas as pd

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

if __name__ == '__main__':
    '''
    EXERCISE 2
    '''
    # df.columns are ['acronym', 'name', 'where']
    df = pd.read_csv('MAY_EXERCISE_1_OUTPUT.csv', sep='\t')
    # Removing duplicates
    df = df.drop_duplicates()
    # Filling mising values.
    # TODO write about fill in missign locations with online, since they all seem to be online journals.
    df['where'] = df['where'].fillna('Online')
    # TODO write about handling this missing city because it wasn't parsed right.
    # Triming whitespace
    for column in df.columns:
        df[column] = df[column].str.strip()
        df[column] = df[column].str.replace('\n', '')
        df[column] = df[column].str.replace('\r', '')
        df[column] = df[column].str.replace('\t', ' ')
        df[column] = df[column].str.replace('.', ',')
        # Replacing '„' with ','. 
        df[column] = df[column].str.replace(chr(132), ',')
        # Replacing '¶' with 'Ö'.
        df[column] = df[column].str.replace(chr(182), chr(214))
    
    # Creating the year column.
    years = []
    for idx, row in df.iterrows():
        try:
            year = int(row['acronym'][-4:])
            years.append(year)
        except:
            raise Exception(row['acronym'], row['name'], row['where'])
    df['year'] = years
    
    # Cleaning up the acronym column
    df['acronym'] = df.apply(lambda row: parse_conference_acronym(row['acronym']), axis=1)

    # Cleaning up the name column
    df['name'] = df.apply(lambda row: parse_conference_name(row['name']), axis=1)

    # Saving the required data for the exercise.
    df[['acronym', 'name', 'where']].to_csv('MAY_EXERCISE_2_OUTPUT.csv', sep='\t', encoding='utf-8', index=False)

    # Saving the data that I will find useful for the rest of the exercises.
    df.to_csv('MAY_conference_data.csv', sep='\t', encoding='utf-8', index=False)

    print("Done")