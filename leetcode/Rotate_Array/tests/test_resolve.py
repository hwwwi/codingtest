#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]), # 7 3 -> 4,
    ([-1,-100,3,99], 2, [3,99,-1,-100]), # 2 4 -> 2
    ([1],0,[1]), # 0 1 -> 0
    ([1,2],1,[2,1]), # 1 2 -> 1
    ([1,2],0,[1,2]), # 0 2 -> 0
    ([1,2],3,[2,1]), # 3 2 -> 1
    ([1,2],4,[1,2]) # 3 2 -> 1
]

@pytest.mark.parametrize("test_input,k, expected", TEST_CASES)
def test_resolve(test_input, k,expected):
    solution = Solution()
    solution.resolve(test_input,k)
    assert test_input == expected
