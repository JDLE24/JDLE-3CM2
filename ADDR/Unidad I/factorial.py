import time
n=0
fac=0
fina= 0
def Facto(n):
    fac=1
    for i in range(1,n+1):
     fac *=i
    print('Resultado de su factorial es: ',fac)
print('Introduzca el numero para sacar factorial: \n', end='')
n= int(input())
Facto(n)
 
