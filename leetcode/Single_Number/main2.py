#!/usr/bin/env python3

from typing import List
from collections import defaultdict

class Solution:
    def resolve(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        for n in nums:
            num_count[n] += 1
        
        for n in num_count:
            if num_count[n] == 1:
                return n