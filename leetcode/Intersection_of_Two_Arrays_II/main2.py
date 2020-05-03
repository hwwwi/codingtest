#!/usr/bin/env python3

from typing import List
from collections import Counter
class Solution:
    def resolve(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        # keep the smallest as nums1
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        # save in a multiset the smallest
        counter = Counter(nums1)
        # find matches, removing from counter when found
        output = []
        for e in nums2:
            if counter[e] > 0:
                output.append(e)
                counter[e] -= 1
        return output