from fourth import calculator,read_yaml
import pytest
from contextlib import nullcontext

@pytest.mark.parametrize(
    "x, y, operator,exception, want",
    [
        (1, 2, "+", nullcontext(), 3),
        (2, 1, "-", nullcontext(), 1),
        (2, 3, "*", nullcontext(), 6),
        (10, 5, "*", nullcontext(), 2),
        ("1", "1", "*", pytest.raises(TypeError), None)

    ]
)

def test_calculator(x, y, exception, want):
    with exception:
        assert calculator(x, y) == want