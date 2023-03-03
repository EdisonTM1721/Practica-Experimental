from os import system

#Clase Arbol para simular el comportamiento de un arbol binnario
class Arbol():
    def __init__(self):
        self.__elemento = ""
        self.__derecha = None
        self.__izquierda = None

    @property
    def elemento(self):
        return self.__elemento
    
    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    @property
    def derecha(self):
        return self.__derecha
    
    @derecha.setter
    def derecha(self, derecha):
        self.__derecha = derecha
    
    @property
    def izquierda(self):
        return self.__izquierda
    
    @izquierda.setter
    def izquierda(self,izquierda):
        self.__izquierda = izquierda
    
    def inorden(self,nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.elemento)
            self.inorden(nodo.derecha)

    def preorden(self,nodo):
        if nodo is not None:
            print(nodo.elemento)
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def postorden(self,nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.elemento)


#Funcion que contiene el menu que se mostrara en pantalla
def menu():
    #Arbol
    arbol = Arbol()
    arbol.elemento = "Pablo"

    #--------------------------------------------------------
    #Rama izquierda
    NodoIzquiero = Arbol()
    NodoIzquiero.elemento = "Pedro"
    arbol.izquierda = NodoIzquiero

    #-----------------------
    #Ramita izquierda de la rama izquierda
    Nodo_I = Arbol()
    Nodo_I.elemento = "Carlos"
    NodoIzquiero.izquierda = Nodo_I

    #-----------
    #rama izquierda de la ramita izquierda
    Nodo = Arbol()
    Nodo.elemento = "Lady"
    Nodo_I.izquierda = Nodo
    #-----------
    #rama derecha de la ramita izquierda
    Nodo = Arbol()
    Nodo.elemento = "Luis"
    Nodo_I.derecha = Nodo

    #-----------------------
    #Ramita derecha de la rama derecha
    Nodo_D = Arbol()
    Nodo_D.elemento = "Pepe"
    NodoIzquiero.derecha = Nodo_D

    #-----------
    #rama izquierda de la ramita derecha
    Nodo = Arbol()
    Nodo.elemento = "Pamela"
    Nodo_D.izquierda = Nodo
    #-----------
    #rama derecha de la ramita derecha
    Nodo = Arbol()
    Nodo.elemento = "Clara"
    Nodo_D.derecha = Nodo

    #--------------------------------------------------------
    #Rama derecha
    NodoDerecho = Arbol()
    NodoDerecho.elemento = "Ramon"
    arbol.derecha = NodoDerecho

    #-----------------------
    #Ramita izquierda de la rama izquierda
    Nodo_I = Arbol()
    Nodo_I.elemento = "Anibal"
    NodoDerecho.izquierda = Nodo_I

    #-----------
    #rama derecha de la ramita izquierda
    Nodo = Arbol()
    Nodo.elemento = "Ines"
    Nodo_I.derecha = Nodo

    #-----------------------
    #Ramita derecha de la rama derecha
    Nodo_D = Arbol()
    Nodo_D.elemento = "Sandra"
    NodoDerecho.derecha = Nodo_D

    #-----------
    #rama derecha de la ramita derecha
    Nodo = Arbol()
    Nodo.elemento = "Juan"
    Nodo_D.derecha = Nodo

    system("cls")
    print("============ RESULTADO ============")
    print("\n--------- INORDEN ----------")
    arbol.inorden(arbol)
    print("\n--------- PREORDEN ----------")
    arbol.preorden(arbol)
    print("\n--------- POSTORDEN ----------")
    arbol.postorden(arbol)

#Se invoca la funcion menu para inciar la ejecucion del programa
menu()
