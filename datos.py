import csv


ARCHIVO_CSV = "paises.csv"


def cargar_paises():
    paises = []

    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }

                    if pais["nombre"] and pais["continente"]:
                        paises.append(pais)

                except ValueError:
                    print("Se encontró un registro con números inválidos y fue omitido.")

                except KeyError:
                    print("El archivo CSV no tiene el formato correcto.")
                    return []

    except FileNotFoundError:
        print("No se encontró el archivo paises.csv.")
        return []

    except Exception as error:
        print("Ocurrió un error al leer el archivo:", error)
        return []

    return paises


def guardar_paises(paises):
    try:
        with open(ARCHIVO_CSV, "w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            escritor.writeheader()
            escritor.writerows(paises)

    except Exception as error:
        print("Ocurrió un error al guardar los datos:", error)


def mostrar_pais(pais):
    print("-" * 40)
    print("Nombre:", pais["nombre"])
    print("Población:", pais["poblacion"])
    print("Superficie:", pais["superficie"], "km²")
    print("Continente:", pais["continente"])


def mostrar_lista_paises(paises):
    if not paises:
        print("No hay países para mostrar.")
        return

    for pais in paises:
        mostrar_pais(pais)