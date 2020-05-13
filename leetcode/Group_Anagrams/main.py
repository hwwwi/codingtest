#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        
        for _, val in enumerate(strs):
            sorted_val = "".join(sorted(val))
            if sorted_val in sorted_strs:
                sorted_strs[sorted_val].append(val)
            else:
                sorted_strs[sorted_val] = [val]
        return list(sorted_strs.values())