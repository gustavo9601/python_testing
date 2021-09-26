from main import *

"""
Ejecutando las pruebas por consola

pip install pytest

pytest <<file_name_test.py>>
"""


def test_fibonacci_5():
    assert fibonacci(5) == 5


def test_palindromo_anita():
    assert palindromo("Anita lava la tina")

def test_factorial_5():
    assert factorial(5) == 120
