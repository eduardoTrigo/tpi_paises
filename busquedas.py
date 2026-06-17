from datos import mostrar_lista_paises

def buscar_pais_por_nombre(paises):

    while True:
        nombre_buscado = input("Ingrese el nombre o parte del nombre del país (0 para cancelar): ").strip().lower()
        
        if nombre_buscado == "0":
            return
        if not nombre_buscado:
            print("Debe ingresar un texto para buscar.")
            continue
        if not nombre_buscado.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
            continue
        break

    resultados = []

    for pais in paises:
        if nombre_buscado in pais["nombre"].lower():
            resultados.append(pais)

    if resultados:
        print("Países encontrados:")
        mostrar_lista_paises(resultados)
    else:
        print("No se encontraron países con ese nombre.")
