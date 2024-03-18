from sys import argv

# argv[1] is the hadoop output file that is needed to be sorted.
input_file = argv[1]
# argv[2] is the desired output file name.
output_file = argv[2]
# argv[3] is the way in which the file should be sorted. 
# The options are 'count', 'list'.
sort_type = argv[3]

# Reading the input file
with open(input_file, 'r') as f:
    data = f.read()

# Parsing and sorting the data
rows = data.split('\n')
# Removing the last empty line.
rows.pop()

def sort_by_count(rows):
    count_idx = 1
    for i in range(len(rows)):
        rows[i] = rows[i].split('\t')
        try:
            rows[i][count_idx] = int(rows[i][count_idx])
        except:
            if count_idx == 2:
                raise Exception(f"Can't convert row[{count_idx}] to an int")
            count_idx = 2
            rows[i][count_idx] = int(rows[i][count_idx])

    rows = sorted(rows, key=lambda row: row[count_idx], reverse=True)
    return rows

def sort_by_list_len(rows):
    for i in range(len(rows)):
        rows[i] = rows[i].split('\t')
        rows[i].append(len(rows[i][1].split(', ')))
    rows = sorted(rows, key=lambda row: row[-1], reverse=True)
    return rows

if sort_type == 'count':
    print(rows[:4])
    rows = sort_by_count(rows)
    print(rows[:4])
else:
    rows = sort_by_list_len(rows)

# Writing output file
with open(output_file, 'w') as f:
    for row in rows:
        line = []
        for cell in row:
            line.append(f"{cell}")
        f.write(f"{'\t'.join(line)}\n")
