from os import system

#Funcion que retorna una lista con los divisiores de un numero
def divisores(numero):
    divisores = []

    for i in range(1,numero):
        if numero % i == 0:
            divisores.append(i)

    divisores.append(numero)

    return divisores

#Funcion la cual contiene el menu que se muestra en pantalla
def menu():
    continuar = ""
    numero = ""

    while(True):
        system("cls")
        print("============ ENCONTRAR DIVISORES ==========")
        while(True):
            try:
                numero = int(input("- Ingrese un numero: "))
                if numero < 0:
                    print("Ingrese numeros positivos!!")
                    continue
            except:
                print("Ingrese numeros no letras!!")
                continue

            break
            
        print("\n============ RESULTADO ===========")
        print(f"- Los divisores del numero '{numero}' son: {divisores(numero)}")

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

#Se invoca a la funcion menu para ejecutar el programa
menu()