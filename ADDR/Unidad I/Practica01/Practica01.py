import time

def main():
    lst=[]
    n=0
    v=0
    print('Determine la longitud de la lista')
    n=int(input())
    for i in range(0,n):
        v=int(input(f"Ingrese el valor {n-i} de la lista: "))
        lst.append(v)
    return(lst)

def br(lst):
    c=0
    lg=len(lst)
    for i in range(0,lg):
            for j in range(0,lg-1):
                 c=c+1
                 if lst[j]>lst[j+1]:
                      a=lst[j]
                      lst[j]=lst[j+1]
                      lst[j+1]=a
    return(lst,c)

def bro(lst):
    c=0
    lg=len(lst)
    cm=lg
    for i in range(0,lg):
            for j in range(0,cm-1):
                 c=c+1
                 if lst[j]>lst[j+1]:
                      a=lst[j]
                      lst[j]=lst[j+1]
                      lst[j+1]=a
            cm=cm-1
    return(lst,c)
        
def ML(lst,c):
     tm=len(lst)
     print("Esta es la lista ordenada")
     for i in range(0,tm):
          print(f"{lst[i]}")
     print(c)
lst=main()
print(''' Determine el tipo de metodo que quiere usar
            Burbuja                  Burbuja optimizada
              (0)                            (1)
''')
chs=int(input())
if chs==0:
    ini=time.time()
    lst,c=br(lst)
    ML(lst,c)
    fin=time.time()
    tmpo=fin-ini
    print(tmpo)  
else:
    ini=time.time()
    lst,c=bro(lst)
    ML(lst,c)
    fin=time.time()
    tmpo=fin-ini
    print(tmpo) 
