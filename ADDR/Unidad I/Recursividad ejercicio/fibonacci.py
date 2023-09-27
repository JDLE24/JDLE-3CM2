def fibo(n):
    if(n==1 or n==0):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
print("Ingrese su numero de posicion de serie de fibonacci")
f=int(input())
print('El numero correspondiente a la posicion dada es: ',fibo(f))

    
