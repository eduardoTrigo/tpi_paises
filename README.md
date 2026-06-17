# Trabajo Práctico Integrador - Programación 1

## Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

### Tecnicatura Universitaria en Programación a Distancia

## Integrantes

* Héctor Eduardo Trigo Estrada
* Dario Curell

## Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python para gestionar datos de países almacenados en un archivo CSV.

El programa permite cargar, consultar, modificar, filtrar, ordenar y analizar información de países utilizando estructuras vistas en Programación 1.

Cada país contiene:

* Nombre
* Población
* Superficie
* Continente

## Tecnologías utilizadas

* Python 3
* Archivos CSV
* Git y GitHub

No se utilizaron librerías externas.

## Conceptos aplicados

* Listas
* Diccionarios
* Funciones
* Condicionales
* Ciclos
* Manejo de archivos CSV
* Validaciones
* Manejo básico de errores
* Ordenamientos
* Estadísticas básicas
* Modularización

## Estructura del proyecto

```text
tpi_paises/
│
├── main.py
├── datos.py
├── validaciones.py
├── busquedas.py
├── filtros.py
├── ordenamientos.py
├── estadisticas.py
├── paises.csv
└── README.md
```

## Funcionalidades

El sistema permite:

1. Mostrar todos los países cargados.
2. Agregar un nuevo país.
3. Actualizar población y superficie de un país.
4. Buscar países por nombre.
5. Filtrar países por continente.
6. Filtrar países por rango de población.
7. Filtrar países por rango de superficie.
8. Ordenar países por nombre, población o superficie.
9. Mostrar estadísticas generales.
10. Guardar los cambios en el archivo CSV.

## Archivo CSV

El archivo `paises.csv` contiene el dataset base del sistema.

Ejemplo:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
Japon,125800000,377975,Asia
```

## Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

En algunos sistemas puede utilizarse:

```bash
python3 main.py
```

## Ejemplo de uso

Al ejecutar el programa se muestra un menú en consola:

```text
MENÚ
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar
5. Ordenar
6. Estadísticas
7. Guardar cambios
0. Salir
```

Ejemplo de búsqueda:

```text
Buscar país: Argentina
Resultado:
Argentina - Población: 45376763 - Superficie: 2780400 - Continente: America
```

## Validaciones realizadas

El programa controla:

* Que los campos no estén vacíos.
* Que población y superficie sean números válidos.
* Que las opciones del menú sean correctas.
* Que las búsquedas sin resultados no generen errores.
* Que el archivo CSV pueda leerse correctamente.
* Que los rangos de filtros sean válidos.

## Organización del trabajo

El proyecto fue dividido en módulos para mantener una estructura clara:

* `main.py`: menú principal y coordinación general.
* `datos.py`: carga, guardado y visualización de datos.
* `validaciones.py`: funciones de validación.
* `busquedas.py`: búsqueda por nombre.
* `filtros.py`: filtros por continente, población y superficie.
* `ordenamientos.py`: ordenamientos.
* `estadisticas.py`: cálculos estadísticos.

## Participación de los integrantes

### Héctor Eduardo Trigo Estrada
### Dario Curell

* Desarrollo de la estructura del proyecto.
* Implementación de módulos principales.
* Pruebas de funcionamiento.
* Documentación del proyecto.
* Revisión del funcionamiento.
* Colaboración en pruebas.
* Participación en documentación.
* Participación en video explicativo.

## Video demostrativo

Link al video:


## Informe PDF

Link o archivo del informe:


## Repositorio

Link del repositorio:

https://github.com/eduardoTrigo/tpi_paises

## Conclusión

El desarrollo de este trabajo permitió integrar los principales contenidos vistos en Programación 1. Se aplicaron listas, diccionarios, funciones, archivos CSV, validaciones, filtros, ordenamientos y estadísticas básicas.

Además, la modularización permitió organizar mejor el código, separando cada responsabilidad en archivos diferentes y facilitando la lectura, el mantenimiento y la explicación del sistema.
