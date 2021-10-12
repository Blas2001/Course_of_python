texto = "Bienvenido al test sobre el queso"# titulo de actividad
print(texto + "\n"+"-"*len(texto)) #metodo len para leer las
#letras de texto y poner "-" debajo de cada letra
print("\n")
puntuacion = 0
opcion = input("""¿Te gusta el queso?
A - No me gusta
B - A veces como queso
C- No puedo evitar de comerlo
¿Cuál es tu respuesta ? """)
if opcion == "A": #condicional anidado
    puntuacion + = 0
elif opcion == "B":
    puntuacion + = 5
elif opcion == "C":
    puntuacion + = 10
else:
    print("No pusiste ninguna opciones correcta ")
    exit() 
print("Tu puntuacion es:{}".format(puntuacion))
exit()
