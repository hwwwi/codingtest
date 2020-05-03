#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for val in set(nums2):
            if val in nums1:
                result += [val] * min(nums1.count(val), nums2.count(val))
        return result