#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (5,[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (0, []),
    (1, [[1]]),
    (2, [[1],[1,1]]),
    (3, [[1],[1,1],[1,2,1]])
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
