from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    if len(libros) == 0:
        return 0
    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)

calcular_promedio_paginas = promedio_paginas

def contar_libros(libros: list[Libro]):
    return len(libros)

def mostrar_disponibles(lista_libros: list[Libro]):
    buscar = False

    for libro in lista_libros:
        if libro["disponible"]:
            print(
                f"Titulo: {libro['titulo']}    -"
                f"Autor: {libro['autor']}       -"
                f"Paginas: {libro['paginas']}  "
            )
            buscar = True
    
    if not buscar:
        print("Por el momento no hay libros disponibles")

filtrar_disponibles = mostrar_disponibles

def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    buscar = False

    for libro in lista_libros:
        if libro["paginas"] < max_paginas:
            print(
                f"Titulo: {libro['titulo']}  -"
                f"Autor: {libro['autor']}    -"
                f"Paginas: {libro['paginas']} "
            )
            buscar = True

    if not buscar:
        print(f"No hay libros con menos de {max_paginas} páginas.")

def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    nueva_categoria = nueva_categoria.strip()

    if not nueva_categoria:
        print("La categoria no debe de estar vacia")
        return

    if nueva_categoria in set_categorias:
        print("La categoria ya existe")
    else:
        set_categorias.add(nueva_categoria)
        print(f"Categoria '{nueva_categoria}' agregada debidamente")