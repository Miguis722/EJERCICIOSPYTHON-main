Saludo = ("Bienvenido al determinador de pares e impares")
print(Saludo)

num_1 = int(input("Por favor, introduzca el número: "))

resultado = (num_1) % (2)

if resultado is 0:
 print("El número es par")
elif resultado is 1 or num_1: 
 print("El número es impar")

