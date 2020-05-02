#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ("anagram","nagaram",True),
    ("rat","car", False),
]

@pytest.mark.parametrize("s,t, expected", TEST_CASES)
def test_resolve(s, t, expected):
    solution = Solution()
    assert solution.resolve(s,t) == expected
