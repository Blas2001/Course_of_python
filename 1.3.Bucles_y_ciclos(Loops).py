#Bucles fuera de la funcion
edades = [18,15,12,45,50]
def verificar_si_puede_conducir(edades):
    if edades >= 18:
        print("usted tien edad suficiente para conducir")
    else:
        print("Usted no tiene edad sufieciente para conducir")
#para cada edad dentro de la lista edades:
for edad in edades:
    verificar_si_puede_conducir(edad)
#Bucle dentro de la funcion
edades1 = [18,15,12,45,50]
def verificar_si_puede_conducir_con_bucles(edades1):
    for edad1 in edades1:
         if edad1 >= 18:
             print("usted tien edad suficiente para conducir")
         else:
              print("Usted no tiene edad sufieciente para conducir")
print("Bucle dentro de la funcion")
verificar_si_puede_conducir_con_bucles(edades1)
