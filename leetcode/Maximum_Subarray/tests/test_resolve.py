#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([1,2], 3),
    ([1,2,3], 6),
    ([1,-1,2,3], 5),
    ([2,3,-1,2,3], 9)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected