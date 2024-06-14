def validar(c):
    vocales = "aeiouAEIOU"
    if c in vocales:
        print(f"EL caracter {c} es vocal")
    else:
        print(f"El caracter {c} no es vocal")
letra = input("Ingresa un caracter: ")

validar(letra)