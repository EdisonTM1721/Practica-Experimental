from os import system

#Funcion para cambiar un numero de una lista por un '*'
def cambiarElemento(lista,n):
    for i in range(len(lista)):
        if lista[i] == n:
            lista[i] = "*"
            return True
    
    return False

#Funcion que contiene el menu que se muestra en pantalla
def menu():
    continuar = ""
    cant = 0
    aux = 0

    while(True):
        lista = []
        system("cls")
        print("=========== LISTA DE NUMEROS ==========")
        while(True):
            try:
                cant = int(input("- ¿Cuantos numeros desea ingresar?: "))
                if cant <= 0:
                    print("Ingrese numero mayores a cero!!")
                else:
                    break
            except:
                print("Ingrese numeros no letras!!")

        print("\n======== NUMEROS ========")
        for i in range(cant):
            while(True):
                try:
                    aux = int(input(f"- numero {i+1}: "))
                    if aux <= 0:
                        print("Ingrese numero mayores a cero!!")
                    else:
                        break
                except:
                    print("Ingrese numeros no letras!!")

            lista.append(aux)

        print("\n=========== CAMBIAR ==========")
        print(f"- Lista: {lista}")
        while(True):
            try:
                aux = int(input("- Ingrese el numero que desea cambiar: "))
                if aux <= 0:
                    print("Ingrese numero mayores a cero!!")
                else:
                    break
            except:
                print("Ingrese numeros no letras!!")

        print("\n========== RESULTADO ===========")
        if cambiarElemento(lista,aux):
            print("- Numero cambiado.")
        else:
            print("- No se encontro el numero en la lista.")
        
        print(f"- Lista: {lista}")
        
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

