from sys import argv

# argv[1] is the hadoop output file that is needed to be sorted.
input_file = argv[1]
# argv[2] is the desired output file name.
output_file = argv[2]

# Reading the input file
with open(input_file, 'r') as f:
    data = f.read()

# Parsing and sorting the data
rows = data.split('\n')
# Removing the last empty line.
rows.pop()
for i in range(len(rows)):
    rows[i] = rows[i].split('\t')
    rows[i][1] = int(rows[i][1])
rows = sorted(rows, key=lambda row: row[1], reverse=True)

# Writing output file
with open(output_file, 'w') as f:
    for row in rows:
        f.write(f"{row[0]}\t{row[1]}\n")
