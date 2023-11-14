import pytest
from src.ej2_3_4 import esEntero

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (100, "Bieen"),
        (47, "Bieen"),
        (-47, "Bieen"),
        (23, "Bieen"),
        (30, "Bieen"),
        (-30, "Bieen"),
        (298, "Bieen"),
        (-298, "Bieen"),
        (88, "Bieen")
    ]
)
def test_esEntero_params(input_n1, expected):
    assert esEntero(input_n1) == expected


def test_esEntero_ValueError():
    with pytest.raises(ValueError):
        esEntero("d")