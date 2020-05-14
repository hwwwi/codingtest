#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([3,2,1,5,6,4],2,5),
    ([3,2,3,1,2,4,5,5,6],4,4),
]

@pytest.mark.parametrize("test_input,k,expected", TEST_CASES)
def test_resolve(test_input,k,expected):
    solution = Solution()
    assert solution.resolve(test_input,k) == expected
