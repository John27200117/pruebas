#Funcion sumatoria
def K(n, p):
    #factor base
    if n == 1: 
        return p
    #factor recursivp
    return n*p + K(n-1, p)
#los inputs para pedir que el usuarios ingresen los numeros
n = int(input("Ingrese un numero n: "))
p = int(input("Ingrese un numero p: "))
print(K(n,p))
