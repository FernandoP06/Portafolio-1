def verificar_divisibilidad(numero):
    divisible_por_3 = (numero % 3 == 0)
    divisible_por_5 = (numero % 5 == 0)
    if divisible_por_3 and divisible_por_5:
        return f"{numero} es divisible por 3 y por 5."
    elif divisible_por_3:
        return f"{numero} es divisible por 3 pero no por 5."
    elif divisible_por_5:
        return f"{numero} es divisible por 5 pero no por 3."
    else:
        return f"{numero} no es divisible ni por 3 ni por 5."
numero = int(input("Introduce un número entero: "))
resultado = verificar_divisibilidad(numero)
print(resultado)

