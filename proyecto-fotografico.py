import json
def editar_servicios():
    with open("photo-campus.json", "r") as archivo:
        servicios_fotografia=json.load(archivo)
    
    print("Editar servicios")
    codigo=int(input("ingrese el codigo del servicio que desea editar:"))
    codigo_encontrado=False
    
    for servicio in servicios_fotografia:
            if servicio["codigo"] == codigo:
                print("servicio encontrado")
                servicio["fecha"] = input("Nueva fecha:")
                servicio["precio"] = float(input("Nuevo precio:"))
                codigo_encontrado=True
                print("su servicio fue actualizado correctamente ")
                break
    if not codigo_encontrado:
        print("no se encontro el servicio amiguibi")
    
    with open("photo-campus.json", "w") as archivo:
        json.dump(servicios_fotografia,archivo)
    