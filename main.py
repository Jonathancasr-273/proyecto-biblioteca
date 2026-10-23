from data.biblioteca import libros, categorias
from utils.operaciones import (
    contar_libros,
    calcular_promedio_paginas,
    filtrar_disponibles,
    buscar_por_paginas
)

def ejecutar_sistema():
    print("=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
    print(f"Total de libros registrados: {contar_libros(libros)}")
    print(f"Promedio de páginas: {calcular_promedio_paginas(libros):.2f}")

    print("\n--- Libros Disponibles ---")
    filtrar_disponibles(libros)

    print("\n--- Libros con menos de 400 páginas ---")
    buscar_por_paginas(libros, 400)

if __name__ == "__main__":
    ejecutar_sistema()