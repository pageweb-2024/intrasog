import matplotlib.pyplot as plt 


def suma (numero1, numero2, numero3):
    resultado = numero1 + numero2 + numero3
    return resultado

def menu():

    while(True):
        print("Menu de opciones")
        print("1. Mostrar datos de infractros")
        print("2. Eliminar datos duplicados")
        print("3. Eliminar datos nulos")
        print("4. Infracciones más comunes (grafico)")
        print("5. mostrar valor de la multa")
        print("6. Salir")

        opcion = input("Ingrese la opcion a elegir")

        if opcion == "1":
            print("1. Se muetra los datos del infractor")
            print()
        elif opcion == "2":
            print("2. Eliminar la infraccion repetida")
            #opcion de los datos repetidos.
        elif opcion == "3":
            print("3. Eliminar datos incompletos")
            #opcion de los datos nulos.
        elif opcion == "4":
            print("4. Muestra el grafico con las infracciones")
            #matplotlib de los datos.
        elif opcion == "5":
            print("5. El infractor quiere saber cuanto hay que pagar")
            numero1 = int(input("ingrese numero 1: "))
            numero2 = int(input("ingrese numero 2: "))
            numero3 = int(input("ingrese numero 3: "))
            resultado = suma(numero1, numero2, numero3)
            print(resultado)
        elif opcion == "6":
            print("6. Cliente sale")
            break
        else:
            print("numero no autorizado intente nuevamente")
                
menu()


