def fact(n):
    if(n==1):
        return 1
    else:
        return fact(n-1)*n
print("Ingrese el numero para evaluar su factorial")
f=int(input())
print('El resultado del factorial solicitado es: ',fact(f))
