#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (["MinStack","push","push","push","getMin","pop","top","getMin"],
    [[],[-2],[0],[-3],[],[],[],[]],
    [None,None,None,None,-3,None,0,-2])
]

@pytest.mark.parametrize("test_action, test_items, expected", TEST_CASES)
def test_resolve(test_action, test_items, expected):
    solution = Solution()
    assert solution.resolve(test_action,test_items) == expected
