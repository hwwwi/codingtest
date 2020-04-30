#!/usr/bin/env python3

from ..main import Solution
from ..main2 import Solution as Solution2
import pytest

TEST_CASES = [
    ([1],1),
    ([2,2,1],1),
    ([4,1,2,1,2],4),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected


@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution2()
    assert solution.resolve(test_input) == expected