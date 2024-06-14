def calcular_salario_neto(salario_bruto):
    if salario_bruto > 2000:
        impuesto = salario_bruto * 0.20
        salario_neto = salario_bruto - impuesto
    else:
        salario_neto = salario_bruto
    return salario_neto
salario_bruto = int(input("Introduce tu salario bruto: $"))
salario_neto = calcular_salario_neto(salario_bruto)
print(f"Tu salario neto después de impuestos es: ${salario_neto:.2f}")
