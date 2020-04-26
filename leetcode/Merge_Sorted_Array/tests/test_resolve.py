#!/usr/bin/env python3

from ..main import Solution
import pytest

TEST_CASES = [
    ([1,2,3,0,0,0],3,[2,5,6],3,[1,2,2,3,5,6]),
    ([1,2,3,0,0,0],3,[1,2,3],3,[1,1,2,2,3,3]),
    ([1,2,3,0,0,0,0],3,[1,2,3],3,[1,1,2,2,3,3])
]

@pytest.mark.parametrize("nums1,m,nums2,n,expected", TEST_CASES)
def test_resolve(nums1,m,nums2,n,expected):
    solution = Solution()
    solution.resolve(nums1,m,nums2,n) == expected
    assert nums1 == expected
