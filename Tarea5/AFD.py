import re

cadena1 = '__servidor1'
cadena2 = '3servidor'
cadena3 = 'servidor3'

def AFD(entrada):

    estado = 0

    for i in range(0,len(entrada)):
        if estado == 0:
            if entrada[i] == '_':
                estado = 1
            elif re.findall("[a-zA-Z]",entrada[i]):
                estado = 2
            else:
                print(f"¡Error!, el caracter '{entrada[i]}' no pertenece al alfabeto del AFD")
        if estado == 1:
            if entrada[i] == '_':
                estado = 1
            elif re.findall("[a-zA-Z]",entrada[i]):
                estado = 3
            else:
                print(f"¡Error!, el caracter '{entrada[i]}' no pertenece al alfabeto del AFD")
        if estado == 2:
            if re.findall("[a-zA-Z]",entrada[i]):
                estado = 2
            elif re.findall("[0-9]",entrada[i]):
                estado = 4
            else:
                print(f"¡Error!, el caracter '{entrada[i]}' no pertenece al alfabeto del AFD")
        if estado == 3:
            if re.findall("[0-9]",entrada[i]):
                estado = 4
            elif re.findall("[a-zA-Z]",entrada[i]):
                estado = 3
            else:
                print(f"¡Error!, el caracter '{entrada[i]}' no pertenece al alfabeto del AFD")
        if estado == 4:
            print(f"'Felicidades, '{entrada}' es una cadena correcta :D ")

AFD(cadena1)
AFD(cadena2)
AFD(cadena3)
