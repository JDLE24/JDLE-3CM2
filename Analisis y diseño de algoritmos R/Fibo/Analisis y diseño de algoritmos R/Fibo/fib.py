import time
fib= []
n=0
def Fibon(num):
    fib.insert(0,1)
    fib.insert(1,1)
    for i in range(2,num):
        next=fib[i-2]+ fib[i-1]
        fib.append(next)
print('Introduzca la posicion de la serie de Fibonacci: \n', end='')
n= input()
n= int(n)
Fibon(n)
print(fib)  
