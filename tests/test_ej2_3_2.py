import pytest
from src.ej2_3_2 import impares

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (100, 99),
        (47, 47),
        (23, 23),
        (30, 29),
        (298, 297),
        (88, 87)
    ]
)
def test_impares_params(input_n1, expected):
    assert impares(input_n1) == expected


def test_impares_ValueError():
    with pytest.raises(ValueError):
        impares(-7)