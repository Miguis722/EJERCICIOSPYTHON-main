Saludo = ("Bienvenido al encontrador del número mayor de tres")
print(Saludo)

num1 = int(input("Por favor, introduzca el primer número"))
num2 = int(input("Por favor, introduzca el segundo número: "))
num3 = int(input("Por favor, introduzca el tercer número"))

if  (num1 > num2) and (num1 > num3):
    Mayor = num1
elif (num2 > num3):
    Mayor = num2
else:
    Mayor = num3
print("El número mayor es:", Mayor)
