"""Given n, find the corresponding value in the Fibonacci sequence."""

import collections
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

    latest_fibonacci_numbers = collections.deque([0, 1], maxlen=2)

    if nth_term < 2:
        result = latest_fibonacci_numbers[nth_term]
    else:
        result = sum(latest_fibonacci_numbers)
        for _ in range(2, nth_term):
            latest_fibonacci_numbers.append(result)
            result = sum(latest_fibonacci_numbers)

    return result


@pytest.mark.parametrize("argument, expected_result", TESTS)
def test_nth_fibonacci(argument, expected_result):
    """Test for the `nth_fibonacci` function."""

    assert nth_fibonacci(argument) == expected_result
