#!/usr/bin/env python3
from typing import List
class Solution:
    def resolve(self, prices: List[int]) -> int:
        result = 0
        length = len(prices)
        for i in range(1, length):
            if prices[i-1] < prices[i]:
                result += prices[i] - prices[i-1]
        return result