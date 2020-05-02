#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3,1],True),
    ([1,2,3,4],False),
    ([1,1,1,3,3,4,3,2,4,2],True),
    ([0,4,5,0,3,6], True)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
