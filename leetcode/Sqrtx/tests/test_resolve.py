#!/usr/bin/env python3

from ..main import Solution as Solution1
from ..main2 import Solution as Solution2
import pytest

TEST_CASES = [
    (4,2),
    (8,2),
    (3,1),
    (1,1),
    (2,1),
    (9,3),
    (16, 4),
    (17, 4)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve1(test_input, expected):
    solution = Solution1()
    assert solution.resolve(test_input) == expected

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve2(test_input, expected):
    solution = Solution2()
    assert solution.resolve(test_input) == expected