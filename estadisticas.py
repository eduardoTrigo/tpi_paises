from datos import mostrar_pais


def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

    total_poblacion = 0
    total_superficie = 0
    cantidad_por_continente = {}

    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    print("\nESTADÍSTICAS GENERALES")

    print("\nPaís con mayor población:")
    mostrar_pais(pais_mayor_poblacion)

    print("\nPaís con menor población:")
    mostrar_pais(pais_menor_poblacion)

    print("\nPromedio de población:", round(promedio_poblacion, 2))
    print("Promedio de superficie:", round(promedio_superficie, 2), "km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in cantidad_por_continente.items():
        print(continente + ":", cantidad)