import json
def agregar_servicios():
    print("Bienvenidos a Photo Campus")
    codigo=int(input("Ingrese un codigo: "))
    nombre=input("Ingrese nombre del servicio fotografico: ")
    precio=int(input("Ingrese el precio: "))

    print("EVENTOS\n1. Boda\n2.Retrato\n3.Productos\n4.Otro")
    evento=int(input("Ingrese evento: "))

    duracion=int(input("Duracion estimada(en horas): "))
    
    datos = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": evento,
        "duracion": duracion
    }

    with open("photo-campus.json", "r") as file:
        dato = json.load(file)

    dato.append(datos)

    with open("photo-campus.json", "w") as file:
        json.dump(dato, file)

    print("Servicio agregado correctamente")


agregar_servicios()

