def convertirHexadecimal(numero):
    conversionCadena = "0123456789ABCDEF"

    if numero < 16:
        respuesta = conversionCadena[numero]
    else:
        respuesta = convertirHexadecimal(numero//16) + conversionCadena[numero%16]
    return respuesta

numero = int(input("Ingrese el numero a convertir: "))
resultado = convertirHexadecimal(numero)
print(resultado)
