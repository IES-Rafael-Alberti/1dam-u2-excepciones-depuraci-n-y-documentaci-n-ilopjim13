import pytest
from src.ej2_3_3 import cuentaAtras

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (100, 0),
        (47, 0),
        (23, 0),
        (30, 0),
        (298, 0),
        (88, 0)
    ]
)
def test_cuentaAtras_params(input_n1, expected):
    assert cuentaAtras(input_n1) == expected


def test_cuentaAtras_ValueError():
    with pytest.raises(ValueError):
        cuentaAtras(-7)