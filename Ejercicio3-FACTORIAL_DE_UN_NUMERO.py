Saludo = ("Bienvenido al exponenciador")
print(Saludo)

def factorial (numero):
  if numero == 0:
    return 1
  else:
    return numero * factorial(numero - 1)
    numero = int(input("Por favor, escriba el nùmero a factorizar: "))
    resultado = factorial (numero)

print("El resultado de la factorializaciòn es de: ", resultado)
