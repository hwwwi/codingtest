#!/usr/bin/env python3
from typing import List

class Solution:
    def resolve(self, nums: List[int], k: int) -> int:
        print(sorted(set(nums), reverse=True))
        return sorted(nums, reverse=True)[k-1]