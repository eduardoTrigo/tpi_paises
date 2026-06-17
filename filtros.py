from datos import mostrar_lista_paises
from validaciones import pedir_entero_positivo


def filtrar_por_continente(paises):
    continente = input("Ingrese el continente: ").strip().lower()

    if not continente:
        print("Debe ingresar un continente.")
        return

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países en ese continente.")


def filtrar_por_rango_poblacion(paises):
    minimo = pedir_entero_positivo("Ingrese población mínima: ")
    maximo = pedir_entero_positivo("Ingrese población máxima: ")

    if minimo > maximo:
        print("El valor mínimo no puede ser mayor que el máximo.")
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países en ese rango de población.")


def filtrar_por_rango_superficie(paises):
    minimo = pedir_entero_positivo("Ingrese superficie mínima: ")
    maximo = pedir_entero_positivo("Ingrese superficie máxima: ")

    if minimo > maximo:
        print("El valor mínimo no puede ser mayor que el máximo.")
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países en ese rango de superficie.")