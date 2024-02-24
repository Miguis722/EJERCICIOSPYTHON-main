Saludo = ("Bienvenido al transformador de Grados Celcius a Fahrenheit")
print(Saludo)

grados = int(input("Por favor, introduzca los grados celcius a transformar: "))

multiplicacion = (grados * 1.8)
fahrenheit = float(multiplicacion + 32)

print(fahrenheit,"°F")
