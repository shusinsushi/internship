import csv

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

file_name = input("Enter the name of the CSV file: ")
read_csv(file_name)
