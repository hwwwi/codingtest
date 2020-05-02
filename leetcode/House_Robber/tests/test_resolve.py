#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3,1],4),
    ([2,7,9,3,1],12),
    ([1], 1),
    ([1,1,1,1], 2),
    ([1,1,1,2], 3),
    ([1,100,100,2], 102),
    ([], 0),
    ([1,2],2),
    ([2,1,1,2],4),
    ([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211], 3365)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
