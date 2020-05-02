#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (1,2,3),
    (4,5,9),
    (-2,3,1),
    (-1,1,0),
    (-3,2,-1),

]

@pytest.mark.parametrize("a,b,expected", TEST_CASES)
def test_resolve(a,b,expected):
    solution = Solution()
    assert solution.resolve(a,b) == expected
