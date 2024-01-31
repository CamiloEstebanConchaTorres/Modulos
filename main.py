# from module.camper import *
# from module.camper import save
# import module.camper as camper
# from module.camper import delete as camp

# import module.camper

# print(dir())
# print(train.save())
# print(train.message())

# print(camp.save("Hola"))
# print(camp.save("camp"))

# print(val.camp)


import module.camper as camper
import module.trainer as trainer
import module.validate as val
import json
from os import system
from module.data import camper as dataCamper
from module.validate import menuNoValid
from module.data import trainer as dataTrainer

def menu():
    print("Sistema de datos de almacenamiento para campus")
    print("\t1. Información del camper")
    print("\t2. Información del trainer")
    print("\t0. Salir")

bandera = True
while (bandera):
    menu()
    opc = int(input())
    match(opc):
        case 1:
            with open("module/Storage/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("clear")
                camper.menu()
        case 2:
            with open("module/Storage/trainer.json", "r") as f:
                trainer.trainer = json.loads(f.read())
                f.close()
                system("clear")
                trainer.menu()
        case 0:
            system("clear")
            bandera = False
        case _:
            print(menuNoValid(opc))



