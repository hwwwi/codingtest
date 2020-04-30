#!/usr/bin/env python3

from typing import List
from collections import defaultdict

class Solution:
    def resolve(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)