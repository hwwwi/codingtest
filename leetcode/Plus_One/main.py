#!/usr/bin/env python3

from typing import List
class Solution:
    def resolve(self, digits:List[int]) -> List[int]:
        reverse = digits[::-1]
        upper = 1
        for idx, val in enumerate(reverse):
            upper, remain = divmod(val + upper, 10)
            reverse[idx] = remain
        if upper:
            reverse.append(upper)
        return reverse[::-1]