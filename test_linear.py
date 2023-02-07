import pytest 

@pytest.mark.parametrize("coord1", "coord2", "x", "y",
    [
        (),
        (),
        ()
    ]
)
def test_linear(coord1, coord2, x, y):
    from linear import linear

    answer = linear(coord1, coord2, x)

    assert answer == y