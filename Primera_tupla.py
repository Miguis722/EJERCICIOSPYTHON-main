#Informacion personal
#Direccion
#Educacion
#Informacion laboral

Saludo = ("Bienvenido a mi primera tupla")
print(Saludo)

nombre = input("Por favor, escriba su nombre: ")
edad = input("Por favor, escriba su edad: ")
direccion = input("Por favor, escriba su direccion: ")
estatura = input("Por favor, escriba su estatura: ")
educacion = input("Por favor, escriba su ultimo nivel de educacion alcanzado: ")
laboral = input("Por favor, escriba si posee experiencia laboral: ")


informacion = tuple((nombre, edad, direccion, estatura, educacion, laboral))
print("De uno en uno", informacion[0::1])
print("De dos en dos", informacion[0::2])
print("De tres en tres", informacion[0::3])
