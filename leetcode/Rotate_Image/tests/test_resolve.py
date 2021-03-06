#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]), 
    ([
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ],
    [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    solution.resolve(test_input)
    assert test_input == expected
