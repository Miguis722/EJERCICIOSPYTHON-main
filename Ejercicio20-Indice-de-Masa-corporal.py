Altura = float(input('ingrese su altura en metros '))
Edad = int(input('ingrese su edad: '))
Peso = float(input('ingrese su peso en kilos: '))

IMC = Peso / (Altura**2)

if Edad<45:
    if IMC < 22:
        print(f"Su condifición de indice de Masa corporal es de: {IMC}. Su riesgo es bajo.")
    elif IMC>=22:
        print(f"Su condifición de indice de Masa corporal es de: {IMC}. Su riesgo es medio")
elif Edad>=45:
    if IMC < 22:
        print(f"Su condifición de indice de Masa corporal es de: {IMC}. Su riesgo es medio.")
    elif IMC>=22:
        print(f"Su condifición de indice de Masa corporal es de: {IMC}. Su riesgo es alto")