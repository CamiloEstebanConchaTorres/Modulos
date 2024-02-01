from os import system
import json
from module.validate import camper
from module.validate import menuNoValid
from .data import camper, generos, trainer

def save():
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n"),
        "Edad": int(input("Ingrese la edad del camper\n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    with open("module/Storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Camper"
def edit():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        * Acualizacion del camper *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas actualizar \n"))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido: {camper[codigo].get('Apellido')}
Edad: {camper[codigo].get('Edad')}
Genero: {camper[codigo].get('Genero')}
________________________
        """)
        print("¿Este es el camper que deseas actualizar? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del camper\n"),
                "Apellido": input("Ingrese el apellido del camper\n"),
                "Edad": int(input("Ingrese la edad del camper\n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
            }
            camper[codigo] = info
            with open("module/Storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera == False
        elif(opc == 3):
            bandera == False
    return "Edit to camper"
def search():
    system("clear")
    print("""
    ********************
    * Lista de Campers *
    ********************
    """)
    for i,val in enumerate(camper):
        print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Edad: {val.get('Edad')}
Genero: {val.get('Genero')}
________________________
        """)
def delete():

    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion del camper  *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas eliminar: \n"))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido: {camper[codigo].get('Apellido')}
Edad: {camper[codigo].get('Edad')}
Genero: {camper[codigo].get('Genero')}
________________________
        """)
        print("¿Este es el camper que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo)
            with open("module/Storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
    return "Camper deleted"
def Asignar():
    system("clear")
    print("""
    ********************
    * Lista de Campers *
    ********************
    """)
    for i,val in enumerate(camper):
        print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Edad: {val.get('Edad')}
Genero: {val.get('Genero')}
________________________

        """)
        codigo = int(input("Ingrese el codigo del camper al que deseas asignarle un trainer \n"))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido: {camper[codigo].get('Apellido')}
Edad: {camper[codigo].get('Edad')}
Genero: {camper[codigo].get('Genero')}
________________________
        """)
        print("¿Este es el camper al que deseas asignarle el trainer ? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
         print("""
    ********************
    * Lista de trainers *
    ********************
    """)
    for indice, elemento in enumerate(trainer):
        print(f"""
________________________
Codigo: {indice}
Nombre: {elemento.get('Nombre')}
Apellido: {elemento.get('Apellido')}
Edad: {elemento.get('Edad')}
Genero: {elemento.get('Genero')}
________________________
""")        
#     codigo = int(input("Ingrese el codigo del trainer que deseas asignarle al camper \n"))
#     print(f"""
#  ________________________
#  Codigo: {codigo}
#  Nombre: {trainer[codigo].get('Nombre')}
#  Apellido: {trainer[codigo].get('Apellido')}
#  Edad: {trainer[codigo].get('Edad')}
#  Genero: {trainer[codigo].get('Genero')}
#________________________
#        """)

#     bandera=True
#     while (bandera):
#         print("""
#         ***************************
#         * Lista de Trainers *
#         ***************************
#         """)
#         codigo = int(input("Ingrese el codigo del trainer que deseas asignarle al camper"))
#         print(f"""
# ________________________
# Codigo: {codigo}
# Nombre: {trainer[codigo].get('Nombre')}
# Apellido: {trainer[codigo].get('Apellido')}
# Edad: {trainer[codigo].get('Edad')}
# Genero: {trainer[codigo].get('Genero')}
# ________________________
#         """)
#         print("¿Este es el trainer que deseas asignarle al camper ?")
#         print("1. Si")
#         print("2. No")
#         print("3. Salir")
#     #     opc = int(input())
#     #     if(opc == 1):
#     #         info = {
#     #             "Nombre": input("Ingrese el nombre del trainer\n"),
#     #             "Apellido": input("Ingrese el apellido del trainer\n"),
#     #             "Edad": int(input("Ingrese la edad del trainer\n")),
#     #             "Genero": input("Elija el genero del trainer:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
#     #         }
#     #         trainer[codigo] = info
#     #         with open("module/Storage/trainer.json", "w") as f:
#     #             data = json.dumps(trainer, indent=4)
#     #             f.write(data)
#     #             f.close()
#     #         bandera == False
#     #     elif(opc == 3):
#     #         bandera == False
#     # return "Edit to camper"
def menu ():

    bandera=True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Guardar camper")
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        print("\t4. Eliminar camper")
        print("\t5. Asignar Trainer")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1: save()
            case 2: search()
            case 3: edit()
            case 4: delete()
            case 5: Asignar()
            case 0:
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))
