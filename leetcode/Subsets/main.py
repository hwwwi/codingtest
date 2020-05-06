#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def subset(pos:int, cur:List[int]):
            res.append(cur)
            for idx, num in enumerate(nums[pos+1:],pos):
                subset(idx+1, cur + [num])
                
        for idx,val in enumerate(nums):
            subset(idx,[val])
        return res