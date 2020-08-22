import json

print("------------------------")
print("----- ARCHIVO JSON -----")
print("------------------------")
print(" ")

def readJson():
    file = open('archivo.json',)
    data = json.load(file)
    file.close()
    print(data)
    print(type(data))
    return data

dict = readJson()
for element in dict:
    print(element)

print(" ")
print(" ")    
