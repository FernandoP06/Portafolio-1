precio = int(input("Ingrese el precio del producto: "))
if precio > 100:
    descuento = precio * 0.10
    precio_final = precio - descuento
    print(f"Se aplicó un descuento del 10%. El precio final es: ${precio_final:.2f}")
else:
    precio_final = precio
    print(f"El precio es menor o igual a $100. El precio final es: ${precio_final:.2f}")
