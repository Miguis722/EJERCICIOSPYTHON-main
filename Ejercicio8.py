Saludo = ("Bienvenido a la serie de Fibonacci")
print(Saludo)

numero = int(input("Por favor, introduzca el número: "))

if numero == 0: 
    numero = int(input("Por favor, introduzca otro número: "))
 

if numero == 1:

    seguir = str(input("¿Desea continuar?(Si o No): "))
    if seguir == "Si":
        resultado = (numero) + (numero)
        resultado1 = (resultado) + (numero)
        resultado2 = (resultado1) + (resultado)
        resultado3 = (resultado2) + (resultado1)
        resultado4 = (resultado3) + (resultado2)
        resultado5 = (resultado4) + (resultado3)
        resultado6 = (resultado5) + (resultado4)
        resultado7 = (resultado6) + (resultado5)
        resultado8 = (resultado7) + (resultado6)
        resultado9 = (resultado8) + (resultado7)
        resultado10 = (resultado9) + (resultado8) 

        print(resultado, "(", (numero), "+", (numero), ")")
        print(resultado1,"(", (resultado), "+", (numero), ")")
        print(resultado2, "(", (resultado1), "+", (resultado), ")")
        print(resultado3, "(", (resultado2), "+", (resultado1), ")")
        print(resultado4, "(", (resultado3), "+", (resultado2), ")")
        print(resultado5, "(", (resultado4), "+", (resultado3), ")")
        print(resultado6, "(", (resultado5), "+", (resultado4), ")")
        print(resultado7, "(", (resultado6), "+", (resultado5), ")")
        print(resultado8, "(", (resultado7), "+", (resultado6), ")")
        print(resultado9, "(", (resultado8), "+", (resultado7), ")")
        print(resultado10, "(", (resultado9), "+", (resultado8), ")" )
