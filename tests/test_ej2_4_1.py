import pytest
from src.ej2_4_1 import ordenarLista

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ([5,4,87,3,1], [1,3,4,5,87]),
        ([7,4,8,3,12], [3,4,7,8,12]),
        ([34,33,28,30,24], [24,28,30,33,34]),
        ([13,4,8,3,12], [3,4,8,12,13]),
        ([20,14,18,13,12], [12,13,14,18,20]),
        ([70,40,80,30,12], [12,30,40,70,80]),
        ([5,4,3,2,1], [1,2,3,4,5]),
        ([7,4,8,3,12,1,14,13,2], [1,2,3,4,7,8,12,13,14])
    ]
)
def test_ordenarLista_params(input_n1, expected):
    assert ordenarLista(input_n1) == expected

