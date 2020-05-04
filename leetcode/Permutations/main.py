#!/usr/bin/env python3

from typing import List
from collections import Counter
class Solution:
    def resolve(self, nums: List[int]) -> List[List[int]]:
        
        visit = {}
        result = []
        length = len(nums)
        for num in nums:
            visit[num] = False

        def permutation(curr: List[int]):
            if len(curr) == length:
                result.append(curr)
                return
            for num in nums:
                if not visit[num]:
                    visit[num] = True
                    permutation(curr + [num])
                    visit[num] = False
                    
        permutation([])
        return result





