import pandas as pd

if __name__ == '__main__':
    # write about consider cases such as empty locations/online, repeatedly posted conferences, etc.
    df = pd.read_csv('MAY_EXERCISE_1_OUTPUT.csv', sep='\t')
    print(df.columns)
    # df.B.unique()
    # boolean = not df["Student"].is_unique      # True (credit to @Carsten)
    # boolean = df['Student'].duplicated().any() # True
    cols = list(df.columns)
    dups = [idx for idx, value in enumerate(df.duplicated()) if value]
    print(dups)
    df = df.drop_duplicates()
    dups = [idx for idx, value in enumerate(df.duplicated()) if value]
    print(dups)
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
            
    print("Done")