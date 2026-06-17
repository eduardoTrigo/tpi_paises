def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if not texto:
            print("Error: el campo no puede estar vacío.")
            continue

        # Permite letras, espacios y acentos
        if not all(caracter.isalpha() or caracter.isspace() for caracter in texto):
            print("Error: solo se permiten letras.")
            continue

        return texto.title()


def pedir_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero

            print("Error: debe ingresar un número mayor a cero.")

        except ValueError:
            print("Error: debe ingresar un número válido.")

        except Exception as error:
            print("Ocurrió un error inesperado:", error)


def pedir_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones_validas:
            return opcion

        print("Opción inválida. Intente nuevamente.")
