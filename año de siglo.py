def es_primer_año_de_siglo(año):
    return año % 100 == 0
año = int(input("Introduce un año: "))
if es_primer_año_de_siglo(año):
    print(f"El año {año} es el primer año de un siglo.")
else:
    print(f"El año {año} no es el primer año de un siglo.")
