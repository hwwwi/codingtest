#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,1,1,2,2,3],2,[1,2]),
    ([1], 1, [1]),
]

@pytest.mark.parametrize("nums, k, expected", TEST_CASES)
def test_resolve(nums, k, expected):
    solution = Solution()
    assert solution.resolve(nums, k) == expected
