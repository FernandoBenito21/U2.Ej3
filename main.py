from ClaseRegistro import *
from claseManejaR import *
import os

def menu():
    print("Menú de opciones:")
    print("0). Concluir")
    print("1). Mostrar para cada variable el día y hora de menor y mayor valor")
    print("2). Indicar la temperatura promedio mensual por cada hora")
    print("3). Dado un número de día listar los valores de las tres variables para cada hora")

if __name__=='__main__':
    medicion=ManejaRegistro()
    medicion.cargararchivo()
    while True:
        os.system('cls')
        menu()
        menu={
              "0":"print('Programa finalizado')",
              "1": "medicion.mayormenor()",
              "2": "medicion.temppromedio()",
              "3": "medicion.listarvalores()",
        }
        opcion=input ("Ingrese una opcion:")
        os.system('cls')
        if opcion in menu:
              if opcion=='4':
                   eval(menu[opcion])
                   break
              else:
                   eval(menu[opcion])
        else:
             print ("La opcion ingresada no existe")

