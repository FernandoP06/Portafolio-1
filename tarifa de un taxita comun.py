def calcular_tarifa_taxi(distancia):
    tarifa_base = 2.50 
    tarifa_adicional = 2.00  
    if distancia <= 10:
        tarifa_total = distancia * tarifa_base
    else:
        tarifa_total = 10 * tarifa_base + (distancia - 10) * tarifa_adicional
    
    return tarifa_total
distancia = int(input("Introduce la distancia recorrida en kilómetros: "))
tarifa = calcular_tarifa_taxi(distancia)
print(f"La tarifa del taxi por recorrer {distancia} kilómetros es: ${tarifa:.2f}")
