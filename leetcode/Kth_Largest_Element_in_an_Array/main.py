#!/usr/bin/env python3
from typing import List
import heapq

class Solution:
    def resolve(self, nums: List[int], k: int) -> int:
        q = []

        for _, val in enumerate(nums):
            heapq.heappush(q, val)
            if len(q) > k:
                heapq.heappop(q)    
        return heapq.heappop(q)