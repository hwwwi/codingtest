#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ("A",1),
    ("B",2),
    ("Z",26),
    ("AA", 27),
    ("AB", 28),
    ("BA", 53),
    ("ZY", 701),
    ("ZZ", 702),
    ("AAA", 703)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
