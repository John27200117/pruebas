#Funcion convertir a cualquier base numerica
def convertirDecimalBase(numero, base):
    #cadena de caracteres para representar el valor de la base
    representacion = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    #Factor base
    if (numero < base):
        respuesta = representacion[numero]
    #factor recursivo
    else:
        respuesta = convertirDecimalBase(numero//base, base) + representacion[numero%base]
    return respuesta
#inputs para pedir el numero a convertir y la base
n = int(input("Ingrese el numero que quiera convertir: "))
p = int(input("Ingrese la base a convertir: "))
print(convertirDecimalBase(n,p))
