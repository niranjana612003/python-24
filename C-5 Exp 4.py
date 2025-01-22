import csv
print("Name : Niranjana S Nair")
print("Roll No: 47")
print("Experiment No: 18")

columns_to_read = [0, 2]
with open('input.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print([row[i] for i in columns_to_read])