#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (10,4), # 2,3,5,7
    (7,3), # 2,3,5
    (15, 6) # 2,3,5,7,11,13
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
