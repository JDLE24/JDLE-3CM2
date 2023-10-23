import matplotlib.pyplot as pl
import numpy as np
import random, time

beg = 0
ta = []
tms = []
for i in range(0,100):

    ta.append(random.randint(10,10000))
def genAr(j):
    argl = []
    for _ in range(ta[j]):
        argl.append(random.randint(0,100))
    return(argl)
def Merge(a1,a2,a3):

    a1.extend(a2)
    a1.extend(a3)
    return a1
def tiem_po(arr):
    beg = time.time()
    QS(arr)
    fn = time.time()
    dif = fn - beg
    tms.append(dif)


def QS(arr):
    if(len(arr)<=1):
        return arr
    else:
        au1 = []
        au2 = []
        au3 = []
        sum = 0
        for i in range(0,len(arr)):
                sum += arr[i]
        mid1 = round(sum/len(arr))
        media = min(arr, key=lambda x: abs(x-mid1))
        arr.pop(arr.index(media))
        au2.append(media)
        for i in range(0,len(arr)):
            if(arr[i]<=media):
                au1.append(arr[i])

            else:

                au3.append(arr[i])
        return Merge(QS(au1),au2,QS(au3))
def QS2(arr):

    if(len(arr)<=1):
        return arr
    else:
        au1 = []
        au2 = []
        au3 = []
        sum = 0
        for i in range(0,len(arr)):
                sum += arr[i]
        piv = arr[0]
        au2.append(piv)
        arr.pop(0)
        for i in range(0,len(arr)):
            if(arr[i]<=piv):
                au1.append(arr[i])
            else:
                au3.append(arr[i])
        return Merge(QS2(au1),au2,QS2(au3))
    

for i in range(0,100):

    tiem_po(genAr(i))
print(tms)
x = np.linspace(0,5,100)
pl.plot(tms)
pl.show()