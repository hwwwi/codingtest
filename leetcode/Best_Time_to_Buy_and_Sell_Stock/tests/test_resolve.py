#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([7,1,5,3,6,4],5),
    ([7,6,4,3,1],0),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
