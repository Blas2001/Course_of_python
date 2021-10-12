vocales = ['a','e','i','o','u']#mi lista
print(vocales) #imprimir lista
vocales.append('l')#agregar una letra al final
print(vocales)#['a','e','i','o','u','l']
vocales.pop()#elimina la ultima letra
print(vocales)#['a','e','i','o','u']
letra = 'f'
print(letra in vocales)# salida: false
