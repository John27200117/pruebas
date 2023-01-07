#Funcion concertir un numero decimal a hexadecimal
def convertirHexadecimal(numero):
    #cadena de caracteres para representar los valores de la base
    conversionCadena = "0123456789ABCDEF"
    #factor base
    if numero < 16:
        respuesta = conversionCadena[numero]
    #factor recursivo
    else:
        respuesta = convertirHexadecimal(numero//16) + conversionCadena[numero%16]
    return respuesta
#input para pedir el numero decimal a convertir
numero = int(input("Ingrese el numero a convertir: "))
resultado = convertirHexadecimal(numero)
print(resultado)
