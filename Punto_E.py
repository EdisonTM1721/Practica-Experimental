from os import system

#Funcion para verificar si la suma de cada columna es igual
def sumarColumnas(matriz,n,m):
    sumas = []
    for i in range(n):
        aux = 0
        for a in range(m):
            aux += matriz[i][a]
        sumas.append(aux)

    return sumas

#Funcion para verificar si las columnas tienen igual suma
def columnasIguales(matriz):
    validar = True
    for i in matriz:
        if matriz[0] != i:
            validar = False
    
    return validar

#Funcionque contiene el menu que se muestra en pantalla
def menu():
    continuar = ""
    n = 0
    m = 0
    aux = 0

    while(True):
        system("cls")
        matriz = []
        print("============== MATRIZ ==============")
        while(True):
            try:
                n = int(input("- Ingrese el numero de columnas: "))
                if n <= 0:
                    print("Ingrese numero mayores a cero!!")
                else:
                    break
            except:
                print("Ingrese numeros no letras!!")

        while(True):
            try:
                m = int(input("- Ingrese el numero de filas: "))
                if m <= 0:
                    print("Ingrese numero mayores a cero!!")
                else:
                    break
            except:
                print("Ingrese numeros no letras!!")

        for i in range(n):
            numeros = []
            print(f"\n=== Columa {i+1} ===")
            for a in range(m):
                while(True):
                    try:
                        aux = int(input(f"Fila {a+1}. Ingrese un numero: "))
                        if aux <= 0:
                            print("Ingrese numero mayores a cero!!")
                        else:
                            break
                    except:
                        print("Ingrese numeros no letras!!")
                numeros.append(aux)
            matriz.append(numeros)

        print("\n============= RESULTADO =============")
        print(f"- Matriz: {matriz}")
        print(f"- Suma de las columnas: {sumarColumnas(matriz,n,m)}")
        if columnasIguales(sumarColumnas(matriz,n,m)):
            print("- La suma de las columnas es igual.")
        else:
            print("- La suma de las columas no es igual.")

        while(True):
            continuar = input("\n¿Desea continuar?(s/n): ")
            continuar.lower()
            if continuar.isalpha() == False:
                print("Ingrese letras no numeros!!")
            elif continuar != "s" and continuar != "n":
                print("Ingrese 's' o 'n'!!")
            else:
                break

        if continuar == "n":
            print("Hasta Pronto!!")
            break

#Se invoca la funcion la funcion menu para comenzar la ejecucion del programa
menu()