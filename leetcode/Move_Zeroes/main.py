#!/usr/bin/env python3

from typing import List
class Solution:
    def resolve(self, nums: List[int]) -> None:
        result = []
        for i in nums:
            if i:
                result.append(i)
        nums[:] = result + [0] * (len(nums) - len(result))