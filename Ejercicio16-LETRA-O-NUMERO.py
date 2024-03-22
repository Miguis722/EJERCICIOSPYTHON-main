def determinarc(texto):
    if texto.isalpha():
        if texto.isupper():
            print("es una letra mayucula.")
        else:
            print("es una letra minuscula")
    elif texto.isdigit():
        print("es un numero.")
    else:
        print("no es ni letra ni numero.")

texto = input("ingrese un escribir")  
determinarc(texto)
