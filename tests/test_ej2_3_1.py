import pytest
from src.ej2_3_1 import edades

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (100, 100),
        (4, 4),
        (5, 5),
        (3, 3),
        (298, 298),
        (88, 88)
    ]
)
def test_edades_params(input_n1, expected):
    assert edades(input_n1) == expected


def test_edades_ValueError():
    with pytest.raises(ValueError):
        edades(-7)
