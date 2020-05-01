#!/usr/bin/env python3

class Solution:
    def resolve(self, n: int) -> int:
        bits = 0
        mask = 1

        for _ in range(32):
            if ((n & mask) != 0):
                bits+=1
            mask <<=1
        return bits;