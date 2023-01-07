def K(n, p):
    if n == 1:
        return p
    return n*p + K(n-1, p)
n = int(input("Ingrese un numero n: "))
p = int(input("Ingrese un numero p: "))
print(K(n,p))
