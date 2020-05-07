#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3,4],[24,12,8,6]),
    ([0,1,2,3],[6,0,0,0]),
    ([1,1,1,1],[1,1,1,1]),
    ([0,0,0,0],[0,0,0,0])
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
