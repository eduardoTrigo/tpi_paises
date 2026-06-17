def pedir_texto(mensaje):
    while True:
        texto = input(f"{mensaje} (0 para cancelar): ").strip()

        if texto == "0":
            return None

        if not texto:
            print("Error: el campo no puede estar vacío.")
            continue

        if not all(caracter.isalpha() or caracter.isspace() for caracter in texto):
            print("Error: solo se permiten letras.")
            continue

        return texto.title()


def pedir_entero_positivo(mensaje):
    while True:
        dato = input(f"{mensaje} (0 para cancelar): ")

        if dato == "0":
            return None

        try:
            numero = int(dato)

            if numero > 0:
                return numero

            print("Error: debe ingresar un número mayor a cero.")

        except ValueError:
            print("Error: debe ingresar solo números.")
            
def pedir_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones_validas:
            return opcion

        print("Opción inválida. Intente nuevamente.")
