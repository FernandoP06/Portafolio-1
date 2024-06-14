caracter = input("Ingrese un carácter: ")
if len(caracter) != 1:
    print("Por favor, ingrese solo un carácter.")
elif caracter.isalpha():
        print(f"El carácter '{caracter}' es una letra.")
elif caracter.isdigit():
        print(f"El carácter '{caracter}' es un dígito.")
else:
        print(f"El carácter '{caracter}' no es ni una letra ni un dígito.")
