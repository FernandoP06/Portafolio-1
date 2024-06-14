def determinar_longitud_nombre(nombre):
    longitud = len(nombre)
    if longitud < 5:
        return "corto"
    elif 5 <= longitud <= 8:
        return "mediano"
    else:
        return "largo"
nombre = input("Introduce un nombre: ")
categoria = determinar_longitud_nombre(nombre)
print(f"El nombre '{nombre}' es de longitud {categoria}.")
