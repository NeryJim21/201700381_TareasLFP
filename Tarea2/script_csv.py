import csv

print("------------------------")
print("----- ARCHIVO  CSV -----")
print("------------------------")
print(" ")

with open('archivo.csv') as f:
    reader = csv.reader(f)
    print(type(reader))
    for row in reader:
        print(row)
        
print(" ")
print(" ")