def es_triangulo_valido(lado1, lado2, lado3):
    return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
lado1 = int(input("Introduce la longitud del primer lado: "))
lado2 = int(input("Introduce la longitud del segundo lado: "))
lado3 = int(input("Introduce la longitud del tercer lado: "))
if es_triangulo_valido(lado1, lado2, lado3):
    print("Las longitudes introducidas forman un triángulo válido.")
else:
    print("Las longitudes introducidas NO forman un triángulo válido.")
