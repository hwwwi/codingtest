#!/usr/bin/env python3
from typing import List
class Solution:
    def resolve(self, nums: List[int]) -> int:
        """
        visit & (1<<k)           -> check
        visit = visit | (1<<k)  -> visit
        """
        visit = 0
        for val in nums:
            if visit & (1<<val):
                return val
            visit = visit | (1<<val)