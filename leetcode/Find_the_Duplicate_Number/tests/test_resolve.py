#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,3,4,2,2],2),
    ([3,1,3,4,2],3),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
