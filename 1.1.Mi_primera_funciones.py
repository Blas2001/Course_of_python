def saludar():
    nombre = input("Digitesu nombre :")
    print(f"hola {nombre} seas bienvenido !!")
saludar()
#concatenar =  es unir dos cadenas de caracteres
def nombre_completo():
   primer_nombre = input('¿Cuál es tu primer nombre? ')
   #El valor del nombre será almacenado en la variable primer_nombre y el valor de apellido en la variable apellido.
   apellido = input('¿Cuál es tu apellido? ')
   nombre_completo = primer_nombre + ' ' + apellido
   #En python, al utilizar el operador suma entre palabras, concatenamos (o unimos) el contenido.
   print(nombre_completo)
nombre_completo()
