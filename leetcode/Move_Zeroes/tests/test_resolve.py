#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([0,1,0,3,12],[1,3,12,0,0]),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    solution.resolve(test_input)
    assert test_input == expected
