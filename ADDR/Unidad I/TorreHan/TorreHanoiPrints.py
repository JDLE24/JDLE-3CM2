def TDH(n,o,d,a):
    if n==1:
        print(n,o,d,a)
        print(f'Movimiento de disc 1 de {o} a {d}')
        print(n,o,d,a)
        return
    print(n,o,d,a)
    TDH(n-1,o,a,d)
    print(n,o,d,a)
    print(f'Movimiento de disc {n} de {o} a {d}')
    print(n,o,d,a)
    TDH(n-1,a,d,o)
    print(n,o,d,a)
n=3
TDH(n,"a","b","c")

