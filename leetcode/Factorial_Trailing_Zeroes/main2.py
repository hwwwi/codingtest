#!/usr/bin/env python3

class Solution:
    def resolve(self, n: int) -> int:
        idx = 5
        count = 0

        while(idx <= n):
            count += (n//idx)
            idx *= 5
        return count


        
