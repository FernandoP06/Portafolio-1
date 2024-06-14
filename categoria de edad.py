edad=int(input("ingrese la edad actual: "))
if edad >= 60:
   print("Eres  un adulto mayor ")
elif edad < 19 and edad >= 13:
   print("Eres  un adolescente")
elif edad < 59 and edad >= 20:
   print("Eres  un adulto")
elif edad < 12:
   print("Eres un  niño")