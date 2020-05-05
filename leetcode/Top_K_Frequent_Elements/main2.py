#!/usr/bin/env python3

from typing import List
from collections import Counter

class Solution:
    def resolve(self, nums:List[int], k:int) -> List[int]:
        counter = Counter(nums)
        res = counter.most_common(k)
        result = [a for a,_ in res]
        return result
