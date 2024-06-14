def determinar_categoria(experiencia):
    if experiencia < 2:
        return "junior"
    elif 2 <= experiencia <= 5:
        return "semi-Senior"
    else:
        return "senior"
experiencia = int(input("Introduce tus años de experiencia: "))
categoria = determinar_categoria(experiencia)
print(f"Con {experiencia} años de experiencia, eres un trabajador {categoria}.")
