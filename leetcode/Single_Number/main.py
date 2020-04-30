#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        idx = 0
        while(idx < length):
            if idx == length -1 or nums[idx] != nums[idx+1]:
                return nums[idx]
            idx += 2