#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (19,True),
    (42,False),
    (0, False),
    (1, True),
    (2, False),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
