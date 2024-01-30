from module.validate import message
from module.validate import menuNoValid
from os import system

def save():
    return "Sucessfully Trainer" + message()

def edit():
    return "Edit to Trainer"

def search():
    return "The Trainer is available"

def delete():
    return "Trainer delete"

def menu():

    bandera = True
    while (bandera):
        print("CRUD del Trainer")
        print("\t1. Guardar Trainer")
        print("\t2. Buscar Trainer")
        print("\t3. Actualizar Trainer")
        print("\t4. Eliminar Trainer")
        print("\t0. Atras")

        opc = int(input())
        match(opc):
            case 1:
                save()
            case 0:
                system("clear")
                bandera = False
            case _:
                print(menuNoValid)
