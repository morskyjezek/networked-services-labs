import csv

with open('data/animal-counts/animals.csv', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    line_count = 0
    for row in data:
        line_count += 1 
        print(f'On {row[0]} there was a count of {row[2]} reported of {row[1]}.')
    print(f'\nRead {line_count} lines.')
