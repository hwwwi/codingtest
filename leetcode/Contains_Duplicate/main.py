#!/usr/bin/env python3

from typing import List
class Solution:
    def resolve(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

