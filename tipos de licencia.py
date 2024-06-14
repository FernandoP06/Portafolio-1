def determinar_tipo_licencia(edad):
    if 16 <= edad <= 17:
        return "Licencia de menor"
    elif 18 <= edad <= 65:
        return "Licencia de adulto"
    elif edad > 65:
        return "Licencia de adulto mayor"
    else:
        return "No es elegible para licencia de conducir"
edad = int(input("Introduce tu edad: "))
tipo_licencia = determinar_tipo_licencia(edad)
print(f"Según tu edad de {edad} años, puedes obtener una {tipo_licencia}.")
