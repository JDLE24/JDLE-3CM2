def burt():
    f=[]
    au=0
    #Pedimos que tan grande se quiere el arreglo y lo agregamos a la variable n
    n= int(input("Inserte la logitud del arreglo: "))
    #hacemos un ciclo for para agregar uno por uno los valores que el usuario desee
    for i in range(0, n):
        ar= int(input(f"Ingrese el valor {i+1} del arreglo: "))
        f.append(ar)
    print("Este es el arreglo sin ordenar: ", f)
    #hacemos dos ciclos, uno para mover un numero hasta donde se necesite y el segundo for es para evaluar y mover los numeros con cada
    # uno de los elementos del arreglo
    for i in range(0,n):
        for j in range(0,n-1):
            if(f[j]>f[j+1]):
                au=f[j]
                f[j]=f[j+1]
                f[j+1]=au
    print("Este es su arreglo ordenado: ", f)
burt()