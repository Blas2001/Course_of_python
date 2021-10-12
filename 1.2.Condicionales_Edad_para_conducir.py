print("Verifico tu edad para saber si puedes conducir")
def verificar_si_puede_conducir():
    Edad=input("Digita tu edad: ")
    Edad=int (Edad)
    if Edad >= 18:
        print("Usted tiene la edad suficienete para conducir")
    else:
        print("usted no tiene edad suficiente para conducir")
verificar_si_puede_conducir()
