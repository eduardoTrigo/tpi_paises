from datos import mostrar_lista_paises


def buscar_pais_por_nombre(paises):
    nombre_buscado = input("Ingrese el nombre o parte del nombre del país: ").strip().lower()

    if not nombre_buscado:
        print("Debe ingresar un texto para buscar.")
        return

    resultados = []

    for pais in paises:
        if nombre_buscado in pais["nombre"].lower():
            resultados.append(pais)

    if resultados:
        print("Países encontrados:")
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países con ese nombre.")