#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (3,0),
    (5,1),
    (10,2),
    (15,3),
    (30,7)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
