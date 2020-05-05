#!/usr/bin/env python3

from typing import List
from collections import Counter
import heapq

class Solution:
    def resolve(self, nums:List[int], k:int) -> List[int]:
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
