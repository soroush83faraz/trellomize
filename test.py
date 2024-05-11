import csv


with open('.venv\\testSavingfile.csv' , 'r') as file:
    
    reader = csv.reader(file)

    header = next(reader)

    rows = []

    for row in reader:
        rows.append(row)

    print(header)
    print(rows)

