#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([0], [1]),
    ([9,9,9], [1,0,0,0]),
    ([8,0,9], [8,1,0]),
    ([7,9,9], [8,0,0]),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
