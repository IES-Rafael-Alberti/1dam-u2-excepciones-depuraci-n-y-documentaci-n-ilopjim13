import pytest
from src.ej2_3_5 import contraseñaCorrecta

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("contra", "Correct Password!!")
        
    ]
)
def test_contraseñaCorrecta_params(input_n1, expected):
    assert contraseñaCorrecta(input_n1) == expected


def test_contraseñaCorrecta_Exception():
    with pytest.raises(Exception):
        contraseñaCorrecta("Contra")
def test_contraseñaCorrecta_Exception2():
    with pytest.raises(Exception):
        contraseñaCorrecta("COntra")
def test_contraseñaCorrecta_Exception3():
    with pytest.raises(Exception):
        contraseñaCorrecta("contrA")