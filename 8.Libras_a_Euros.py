print("Cambio de Libras a Euros") #Titulo de programa
Libras =  float(input("Introduce Las Libras: "))#pedimos las libras a convertir
Cambio =  float(input("Introduce Las el valor de cambio: "))#introducimos el tipo de cambio
Euros = Libras*Cambio #Hacemo el proceso para sacar Euros
print("Las Libras: {}  a Euros: {}".format(Libras,Euros))
##imprimimos las libras con la funcion .format para integrat un integer a una cadena de caracteres 
