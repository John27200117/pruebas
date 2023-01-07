def convertirDecimalBase(numero, base):

    representacion = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if (numero < base):
        respuesta = representacion[numero]
    else:
        respuesta = convertirDecimalBase(numero//base, base) + representacion[numero%base]
    return respuesta

n = int(input("Ingrese el numero que quiera convertir: "))
p = int(input("Ingrese la base a convertir: "))
print(convertirDecimalBase(n,p))
