from agregar import agregar_servicios
from editar import editar_servicios
from eliminar import eliminar_servicio

opciones=int(input("Opciones\n1.Agregar servicio.\n2.Editar servicio.\n3.Eliminar servicios\nIngrese la opcion que desea: "))
match opciones:
    case 1:
        if opciones== 1:
            agregar_servicios()
    case 2:
        if opciones== 2:
            editar_servicios()
    case 3:
        if opciones== 3:
            eliminar_servicio()
    #