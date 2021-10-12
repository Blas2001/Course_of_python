verificaciones =[]
edades =[13,15,20]
def verificar_si_puede_conducir_bool(verificaciones,edades):
    for edad in edades:
         if edad >= 18:
             verificaciones.append(True)
         else:
              verificaciones.append(False)
verificar_si_puede_conducir_bool(verificaciones,edades)
print(verificaciones)

def verificar_si_puede_conducir(Verificaciones):
    for drive in verificaciones:
        if drive == True:
            print("usted tien edad suficiente para conducir")
        else:
            print("Usted no tiene edad sufieciente para conducir")
print(verificar_si_puede_conducir(verificaciones))
