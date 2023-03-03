from os import system

#Clase Pila para simular el comportamiento de una pila
class Pila():
    def __init__(self):
        self.pila = []

    def empilar(self,elemento):
        self.pila.insert(0,elemento)

    def pilaVacia(self):
        return len(self.pila) == 0
    
    def desempilar(self):
        if self.pilaVacia():
            return False
        else:
            self.pila.pop(0)
            return True
        
    def vaciarPilar(self):
        if self.pilaVacia():
            return False
        else:
            for i in range(len(self.pila)):
                self.desempilar()
    
    def getPila(self):
        return self.pila
    
    def getPilaASCII(self):
        pilaASCII = []
        for i in self.pila:
            pilaASCII.append(ord(i))

        return pilaASCII

#Funcion que contiene el menu que se mostrara en pantalla
def menu():
    continuar = ""
    pila = Pila()
    aux = ""

    while(True):
        pila.vaciarPilar()
        system("cls")
        print("============ PILA ASCII ===========")
        while(True):
            aux = input("- Ingrese un caracter: ")
            if aux == "*":
                break
            else:
                pila.empilar(aux)

        print("\n============ RESULTADO ============")
        print(f"- Pila: {pila.getPila()}")
        print(f"- Pila ASCII: {pila.getPilaASCII()}")

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
