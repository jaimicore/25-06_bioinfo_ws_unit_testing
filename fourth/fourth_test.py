from fourth.fourth import calculator,read_yaml
import pytest
from contextlib import nullcontext

@pytest.mark.parametrize(
    "x, y, operator, exception, want",
    [
        (1, 2, "addition", nullcontext(), 3),
        (2, 1, "subtraction", nullcontext(), 1),
        (2, 3, "multiplication", nullcontext(), 6),
        (10, 5, "division", nullcontext(), 2),
        ("1", "1", "addition", pytest.raises(TypeError), None)
#        (10, 5, "/", pytest.raises(TypeError), pytest.raises(TypeError))

    ]
)

def test_calculator(x, y, operator, exception, want):
    with exception:
        assert calculator(x, y, operator) == want