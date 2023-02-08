import pytest 

testdata = [
    ((1, 2), (2, 2), 5, 2),
    ((0, 0), (1, 1), 3, 3),
    ((0, 0), (2, 1), 4, 2),
]

@pytest.mark.parametrize("coord1, coord2, x, y", testdata)
def test_linear(coord1, coord2, x, y):
    from linear import linear

    answer = linear(coord1, coord2, x)

    assert answer == y