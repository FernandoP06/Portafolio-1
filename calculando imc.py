def calcular_imc(peso, altura):
    return peso / (altura ** 2)
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
peso = int(input("Introduce tu peso en kilogramos: "))
altura = int(input("Introduce tu altura en metros: "))
imc = calcular_imc(peso, altura)
categoria_imc = clasificar_imc(imc)
print(f"tu IMC es {imc:.2f}, lo que indica que tienes {categoria_imc}.")
