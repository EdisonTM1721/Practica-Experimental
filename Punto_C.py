from os import system

#Funcion de ordenamiento por insercion
def insercion(lista):
    aux = 0
    for i in range(len(lista)):
        for a in range(len(lista)):
            if lista[i] < lista[a]:
                aux = lista[i]
                lista[i] = lista[a]
                lista[a] = aux

    return lista

#Funcion que contiene el menu que se muestra en pantalla
def menu():

    numeros = [5,99,12,5,36,-96,54,1]

    system("cls")
    print("========== ORDENAIMENTO POR INSERCION ==========")
    print(f"- Lista de numeros: {numeros}")
    print(f"- Lista de numeros ordenada: {insercion(numeros)}")

#se invoca la funcion menu para comenzar la ejecucion del programa
menu()
                
