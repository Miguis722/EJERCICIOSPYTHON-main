def año_bisiesto(año):
    if año %4 ==0 and (año!=0 or año%400 ==0):
        return True
    else:
        return False
    
año =int(input("Indique el año: "))
if año_bisiesto(año):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")