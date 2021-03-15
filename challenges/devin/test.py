"""Test suite for pytest."""

# The following line tells our "pylint" linter to ignore a few coding best practices.
#
# Disabling "import-outside-toplevel" ignores the fact that we're doing "imports" inside
# functions instead of the top of the file. We are doing this because we want to "scope"
# our imports to individual tests to avoid polluting the global test namespace.
#
# Disabling "missing-function-docstring" ignores the fact that we're not documenting our
# functions. For now, the function names of the tests are sufficient, and requiring us
# to add a docstring to every function would be repetitive.

# pylint: disable=import-outside-toplevel, missing-function-docstring


def test_nth_fibonacci():
    import d01_nth_fibonacci as d01

    assert d01.nth_fibonacci(d01.NTH_TERM) == d01.EXPECTED_OUTPUT
