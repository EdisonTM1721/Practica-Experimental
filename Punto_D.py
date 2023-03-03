from os import system

#Funcion para crear una matriz y rellenarla de numeros
def CrearMatriz(n):
    matriz = []
    
    cont = 0
    for i in range(n):
        numeros = []
        for a in range(n):
            numeros.append(cont)
            cont += 1
        matriz.append(numeros)

    return matriz

#Funcion que contiene le menu que se mostrara en pantalla
def menu():
    continuar = ""
    tamano = 0

    while(True):
        system("cls")
        print("=========== CREAR MATRIZ =========")
        while(True):
            try:
                tamano = int(input("- Ingrese el tamano de la matriz: "))
                if tamano <= 0:
                    print("Ingrese numero mayores a cero!!")
                else:
                    break
            except:
                print("Ingrese numeros no letras!!")

        print("\n========== MATRIZ =========")
        print(f"- Matriz: {CrearMatriz(tamano)}")

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

#Se invoca a la funcion menu para comenzar la ejecucion del programa
menu()
