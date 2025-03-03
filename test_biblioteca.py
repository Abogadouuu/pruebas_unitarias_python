# test_operaciones.py
from biblioteca import *
import pytest

def test_titulo_libro():
    libro_test = Libro("prueba","prueba_autor","2025")
    assert libro_test.titulo

def test_autor_libro():
    libro_test = Libro("prueba","prueba_autor","2025")
    assert libro_test.autor

def test_anio_libro():
    libro_test = Libro("prueba","prueba_autor","2025")
    assert libro_test.anio

def test_prestado_libro():
    libro_test = Libro("prueba","prueba_autor","2025")
    assert isinstance(libro_test.prestado,bool)

def test_agregar_libro():
    prueba_biblioteca = Biblioteca()
    assert prueba_biblioteca.agregar_libro(Libro("prueba","prueba_autor","2025")) is None

def test_agregar_libro_argumentos_distintos():
    prueba_biblioteca = Biblioteca()
    assert prueba_biblioteca.agregar_libro(Libro(23,90.5,2025)) is None

def test_eliminar_libro():
    prueba_biblioteca = Biblioteca()
    # Primero se crea el libro para eliminarlo despues
    prueba_biblioteca.agregar_libro(Libro("prueba_eliminar","prueba_autor","2025"))
    assert prueba_biblioteca.eliminar_libro("prueba_eliminar") is None

def test_eliminar_libro_inexistente():
    prueba_biblioteca = Biblioteca()
    assert prueba_biblioteca.eliminar_libro("prueba_sin_existir") is None

def test_buscar_libro():
    prueba_biblioteca = Biblioteca()
    # Primero se crea el libro para buscarlo despues
    prueba_biblioteca.agregar_libro(Libro("prueba_buscar","prueba_autor","2025"))
    assert isinstance(prueba_biblioteca.buscar_libro("prueba_buscar"), Libro)

def test_buscar_libro_inexistente():
    prueba_biblioteca = Biblioteca()
    assert prueba_biblioteca.buscar_libro("prueba_sin_existir") is None

def test_listar_libro():
    prueba_biblioteca = Biblioteca()
    assert isinstance(prueba_biblioteca.listar_libros(), list)

def test_prestar_libro():
    prueba_biblioteca = Biblioteca()
    # Primero se crea el libro para prestarlo despues
    prueba_biblioteca.agregar_libro(Libro("prueba_prestar","prueba_autor","2025"))
    assert prueba_biblioteca.prestar_libro("prueba_prestar")

def test_prestar_libro_prestado():
    prueba_biblioteca = Biblioteca()
    # Primero se crea el libro para prestarlo despues
    prueba_biblioteca.agregar_libro(Libro("prueba_prestar","prueba_autor","2025"))
    # Se presta el libro,la primera vez para contarlo como prestado y la segunda para realizar la prueba
    prueba_biblioteca.prestar_libro("prueba_prestar")
    assert isinstance(prueba_biblioteca.prestar_libro("prueba_prestar"), str)

def test_prestar_libro_inexistente():
    prueba_biblioteca = Biblioteca()
    assert isinstance(prueba_biblioteca.prestar_libro("prueba_sin_existir"), str)

def test_devolver_libro():
    prueba_biblioteca = Biblioteca()
    # Primero se crea el libro para prestarlo despues
    prueba_biblioteca.agregar_libro(Libro("prueba_devolver","prueba_autor","2025"))
    # se presta el libro para devolverlo despues
    prueba_biblioteca.prestar_libro("prueba_devolver")
    assert prueba_biblioteca.devolver_libro("prueba_devolver")

def test_devolver_libro_no_prestado():
    prueba_biblioteca = Biblioteca()
    # Primero se crea el libro para devolverlo despues
    prueba_biblioteca.agregar_libro(Libro("prueba_devolver","prueba_autor","2025"))
    assert isinstance(prueba_biblioteca.devolver_libro("prueba_devolver"), str)

def test_devolver_libro_inexistente():
    prueba_biblioteca = Biblioteca()
    assert prueba_biblioteca.devolver_libro("prueba_sin_existir")

if __name__ == "__main__":
    pytest.main()