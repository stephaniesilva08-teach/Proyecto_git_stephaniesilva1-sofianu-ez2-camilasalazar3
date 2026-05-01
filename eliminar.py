def eliminar_servicio():
    import json

    ARCHIVO = "photo-campus.json"

    try:
        with open(ARCHIVO, "r") as archivo:
            servicios = json.load(archivo)
    except FileNotFoundError:
        servicios = []

    if not servicios:
        print("No hay servicios registrados.")
        return

    codigo = input("Ingrese el código del servicio que quieres eliminar: ").strip()

    for servicio in servicios:
        if servicio["codigo"] == codigo:
            servicios.remove(servicio)
            with open(ARCHIVO, "w") as archivo:
                json.dump(servicios, archivo)
            print("Servicio eliminado correctamente.")
            return

    print("No se encontró un servicio con ese código.")




    



























