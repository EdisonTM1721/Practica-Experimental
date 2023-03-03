from os import system

#Funcion para saber un palabra es polindorma
def palindroma(palabra):
    inversa = ""
    for i in palabra:
        inversa = i + inversa

    return inversa == palabra

#Funcion que contiene el menu que se mueestra en pantalla
def menu():
    continuar = ""
    palabra = ""

    while(True):
        system("cls")
        print("=========== PALABRA PALINDROMA ===========")
        palabra = input("- Ingrese una palabra: ")

        print("\n=========== RESULTADO ===========")
        print(f"- La palabra '{palabra}' es: ",end="")
        if palindroma(palabra):
            print("Es palindroma.")
        else:
            print("No es palindroma.")

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