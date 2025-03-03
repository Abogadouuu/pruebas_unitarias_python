# test_operaciones.py
from cine import *
import pytest

def test_venta_normal_entradas():
    assert isinstance(Pelicula.vender_entradas(pelicula1,3), str)

def test_venta_excesiva_entradas():
    assert isinstance(Pelicula.vender_entradas(pelicula1,30000), str)

def test_venta_nula_entradas():
    assert isinstance(Pelicula.vender_entradas(pelicula1,0), str)

def test_venta_negativa_entradas():
    assert isinstance(Pelicula.vender_entradas(pelicula1,-188), str)

def test_venta_String_entradas():
    assert isinstance(Pelicula.vender_entradas(pelicula1,"3"), str)

def test_venta_decimal_entradas():
    assert isinstance(Pelicula.vender_entradas(pelicula1,3.3), str)

if __name__ == "__main__":
    pytest.main()