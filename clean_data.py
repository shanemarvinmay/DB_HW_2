import pandas as pd

if __name__ == '__main__':
    # write about consider cases such as empty locations/online, repeatedly posted conferences, trim whitespace, etc.
    df = pd.read_csv('MAY_EXERCISE_1_OUTPUT.csv', sep='\t')
    # Removing duplicates
    df = df.drop_duplicates()
    # Filling mising values.
    # TODO write about fill in missign locations with online, since they all seem to be online journals.
    df['where'] = df['where'].fillna('Online')
    # TODO write about handling this missing city because it wasn't parsed right.
    # where JÃ¶nkÃ¶ping ->  Jönköping
    # df['where'] = df['where'].map({'JÃ¶nkÃ¶ping': 'Jönköping'})
    # Triming whitespace
    for column in df.columns:
        df[column] = df[column].str.strip()
        df[column] = df[column].str.replace('\n', '')
        df[column] = df[column].str.replace('\r', '')
        df[column] = df[column].str.replace('\t', ' ')
        df[column] = df[column].str.replace('.', ',')
        # replacing „
        df[column] = df[column].str.replace(chr(132), ',')
        # replace ¶ with Ö
        df[column] = df[column].str.replace(chr(182), chr(214))
    # Checking to make sure whitespace has been stripped.
    for idx, row in df.iterrows():
        for col in df.columns:
            print(f"|{row[col]}|", end='\t')
        print()
    # missing value stuff
    # print(df.columns) ['acronym', 'name', 'where']
    # where nan
    for col in df.columns:
        if df[col].isnull().values.any():
            print(col)
    for idx, row in df.iterrows():
        # if pd.isna(row['where']) and 'ournal' not in row['name']:
        #     print(row['acronym'], row['name'])  
        if row['where'] == 'JÃ¶nkÃ¶ping':
            for i in row['where']:
                print(i, ord(i))
            print(row['acronym'], row['name'])  
        # if row['where'] == 'Mainz, Germany (Rheingoldhalle) & online':
        #     for i in row['name']:
        #         print(i, ord(i))
    # duplicate stuff
    # a = df['A'].unique()
    # print(sorted(a))
    # df.B.unique()
    # boolean = not df["Student"].is_unique      # True (credit to @Carsten)
    # boolean = df['Student'].duplicated().any() # True
    # cols = list(df.columns)
    # dups = [idx for idx, value in enumerate(df.duplicated()) if value]
    # print(dups)    
    # dups = [idx for idx, value in enumerate(df.duplicated()) if value]
    # print(dups)
    # for idx, row in df.iterrows():
    #     if idx in dups:
    #         print(row)
    # for col in cols:
    #     if df[col].is_unique:
    #         continue
    #     print(col)
    #     dups = df[col].duplicated()
    #     dup_ids = set()
    #     for i in range(len(dups)):
    #         if dups[i]:
    #             dup_ids.add(i)
    #     for id, row in df.iterrows():
    #         if  id in dup_ids:
    #             print(row[col])
    df[['acronym', 'name', 'where']].to_csv('MAY_EXERCISE_2_OUTPUT.csv', sep='\t', encoding='utf-8', index=False)
    print("Done")