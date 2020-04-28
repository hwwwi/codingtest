#!/usr/bin/env python3
from typing import List
class Solution:
    def resolve(self, prices: List[int]) -> int:
        if not prices:
            return 0
        result = 0
        pivot = prices[0]
        for price in prices[1:]:
            if price < pivot:
                pivot = price
            else:
                result = max(result, price - pivot)
        return result
