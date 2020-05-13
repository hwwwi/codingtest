#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert sorted(solution.resolve(test_input)) == sorted(expected)
