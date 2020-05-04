#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3],[
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]),
    ([1,2], [
        [1,2],
        [2,1]
    ])
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert sorted(solution.resolve(test_input)) == sorted(expected)
