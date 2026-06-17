from datos import mostrar_lista_paises
from validaciones import pedir_opcion


def elegir_orden():
    print("1. Ascendente")
    print("2. Descendente")

    opcion = pedir_opcion("Seleccione el tipo de orden: ", ["1", "2"])

    return opcion == "2"


def ordenar_por_nombre(paises):
    descendente = elegir_orden()
    paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"], reverse=descendente)

    mostrar_lista_paises(paises_ordenados)


def ordenar_por_poblacion(paises):
    descendente = elegir_orden()
    paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)

    mostrar_lista_paises(paises_ordenados)


def ordenar_por_superficie(paises):
    descendente = elegir_orden()
    paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)

    mostrar_lista_paises(paises_ordenados)