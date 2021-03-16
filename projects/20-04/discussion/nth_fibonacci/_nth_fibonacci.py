"""Given n, find the corresponding value in the Fibonacci sequence."""

from collections import deque

import pytest

TESTS = [
    # (argument, expected_result)
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (24, 46368),
]


def nth_fibonacci(nth_term: int) -> int:
    """Given n, find the corresponding value in the Fibonacci sequence."""

    pass


@pytest.mark.parametrize("argument, expected_result", TESTS)
def test_nth_fibonacci(argument, expected_result):
    """Test for `nth_fibonacci`."""

    assert nth_fibonacci(argument) == expected_result
