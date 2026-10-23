from models.libro import Libro


libros: list[Libro] = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "paginas": 471, "disponible": True},
    {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "paginas": 96, "disponible": True},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "paginas": 863, "disponible": False},
    {"titulo": "1984", "autor": "George Orwell", "paginas": 328, "disponible": True},
]


categorias: set[str] = {"Ficción", "Clásicos", "Distopía"}