#!/usr/bin/env python3

from ..main import Solution
from ..main import Solution as Solution2
import pytest

TEST_CASES = [
    ("A man, a plan, a canal: Panama",True),
    ("race a car",False),
    ("", True),
    ("abc", False),
    ("abcba", True),
    ("abccba", True),
    ("09", False),
    ("00", True)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected


@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolv2(test_input, expected):
    solution = Solution2()
    assert solution.resolve(test_input) == expected