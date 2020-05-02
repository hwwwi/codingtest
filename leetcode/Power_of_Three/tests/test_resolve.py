#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (19682,False),
    (19684,False),
    (0,False),
    (3, True),
    (27, True),
    (45, False),
    (2, False),
    (1, True),
    (6, False)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
