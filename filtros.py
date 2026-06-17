from datos import mostrar_lista_paises
from validaciones import pedir_entero_positivo


def filtrar_por_continente(paises):
    while True:
        continente = input("Ingrese el continente (0 para cancelar): ").strip().lower()
        if continente == "0":
            return
        
        if not continente:
            print("Debe ingresar un continente.")
            continue

        if not continente.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
            continue
        
        break

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países en ese continente.")


def filtrar_por_rango_poblacion(paises):

    while True:

        minimo = pedir_entero_positivo("Ingrese población mínima:")
        if minimo is None:
            return

        maximo = pedir_entero_positivo("Ingrese población máxima:")
        if maximo is None:
            return

        if minimo <= maximo:
            break

        print("Error: el mínimo no puede ser mayor que el máximo.")

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países en ese rango de población.")


def filtrar_por_rango_superficie(paises):

    while True:

        minimo = pedir_entero_positivo("Ingrese superficie mínima:")
        if minimo is None:
            return

        maximo = pedir_entero_positivo("Ingrese superficie máxima:")
        if maximo is None:
            return

        if minimo <= maximo:
            break

        print("Error: el mínimo no puede ser mayor que el máximo.")

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países en ese rango de superficie.")
