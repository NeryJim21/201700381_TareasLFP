from xml.dom import minidom

print("------------------------")
print("----- ARCHIVO XML  -----")
print("------------------------")
print(" ")

doc = minidom.parse("archivo.xml")

#PAdre:
item = doc.getElementsByTagName("participante")

print()
for participante in item:

    item_nombre = participante.getElementsByTagName("nombre") [0]

    item_lugar = participante.getElementsByTagName("lugar") [0]

    item_nacionalidad = participante.getElementsByTagName("nacionalidad") [0]

    item_edad = participante.getElementsByTagName("edad") [0]

    #Imprimir datos:

    print("Nombre: ", item_nombre.firstChild.data)
    print("Lugar: ", item_lugar.firstChild.data)
    print("Nacionalidad: ", item_nacionalidad.firstChild.data)
    print("Edad: ", item_edad.firstChild.data)

print()
print(type(doc))
print(" ")
print(" ")