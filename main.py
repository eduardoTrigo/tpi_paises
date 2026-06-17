from datos import cargar_paises, guardar_paises, mostrar_lista_paises
from validaciones import pedir_texto, pedir_entero_positivo, pedir_opcion
from busquedas import buscar_pais_por_nombre
from filtros import (
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie
)
from ordenamientos import (
    ordenar_por_nombre,
    ordenar_por_poblacion,
    ordenar_por_superficie
)
from estadisticas import mostrar_estadisticas


def agregar_pais(paises):
    print("\nAGREGAR PAÍS")

   nombre = pedir_texto("Ingrese nombre del país: ")

for pais in paises:
    if pais["nombre"].lower() == nombre.lower():
        print("Error: ese país ya existe.")
        return
            
    poblacion = pedir_entero_positivo("Ingrese población: ")
    superficie = pedir_entero_positivo("Ingrese superficie en km²: ")
    continente = pedir_texto("Ingrese continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_paises(paises)

    print("País agregado correctamente.")

    poblacion = pedir_entero_positivo("Ingrese población: ")
    superficie = pedir_entero_positivo("Ingrese superficie en km²: ")
    continente = pedir_texto("Ingrese continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_paises(paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):
    print("\nACTUALIZAR PAÍS")

    nombre = pedir_texto("Ingrese el nombre exacto del país a actualizar: ").lower()

    pais_encontrado = None

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print("No se encontró un país con ese nombre.")
        return

    print("País encontrado:", pais_encontrado["nombre"])

    nueva_poblacion = pedir_entero_positivo("Ingrese nueva población: ")
    nueva_superficie = pedir_entero_positivo("Ingrese nueva superficie en km²: ")

    pais_encontrado["poblacion"] = nueva_poblacion
    pais_encontrado["superficie"] = nueva_superficie

    guardar_paises(paises)

    print("Datos actualizados correctamente.")


def menu_filtros(paises):
    while True:
        print("\nMENÚ DE FILTROS")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("4. Volver al menú principal")

        opcion = pedir_opcion("Seleccione una opción: ", ["1", "2", "3", "4"])

        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "3":
            filtrar_por_rango_superficie(paises)
        elif opcion == "4":
            break


def menu_ordenamientos(paises):
    while True:
        print("\nMENÚ DE ORDENAMIENTOS")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("4. Volver al menú principal")

        opcion = pedir_opcion("Seleccione una opción: ", ["1", "2", "3", "4"])

        if opcion == "1":
            ordenar_por_nombre(paises)
        elif opcion == "2":
            ordenar_por_poblacion(paises)
        elif opcion == "3":
            ordenar_por_superficie(paises)
        elif opcion == "4":
            break


def mostrar_menu_principal():
    print("\n" + "=" * 45)
    print("GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 45)
    print("1. Mostrar todos los países")
    print("2. Agregar país")
    print("3. Actualizar país")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Salir")


def main():
    paises = cargar_paises()

    while True:
        mostrar_menu_principal()

        opcion = pedir_opcion("Seleccione una opción: ", ["1", "2", "3", "4", "5", "6", "7", "8"])

        if opcion == "1":
            mostrar_lista_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais_por_nombre(paises)

        elif opcion == "5":
            menu_filtros(paises)

        elif opcion == "6":
            menu_ordenamientos(paises)

        elif opcion == "7":
            mostrar_estadisticas(paises)

        elif opcion == "8":
            print("Programa finalizado. Muchas gracias.")
            break


main()
