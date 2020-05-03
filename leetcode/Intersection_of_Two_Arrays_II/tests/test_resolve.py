#!/usr/bin/env python3

from ..main import Solution
from ..main2 import Solution as Solution2
import pytest

TEST_CASES = [
    ([1,2,2,1],[2,2],[2,2]),
    ([4,9,5],[9,4,9,8,4],[9,4]),
    ([1,1,1],[1,1,1],[1,1,1]),
    ([1],[],[]),
    ([1],[1],[1]),
    ([4,9,5], [4,9,4,9,5], [9,4,5]),
    ([4,9,5], [4,9,5,9,4], [9,4,5]),
    ([1,2,2,1],[2],[2]),
    ([3,1,2], [1,1], [1])
]

@pytest.mark.parametrize("num1, num2, expected", TEST_CASES)
def test_resolve(num1, num2, expected):
    solution = Solution()
    assert solution.resolve(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", TEST_CASES)
def test_resolve2(num1, num2, expected):
    solution = Solution2()
    assert solution.resolve(num1, num2) == expected