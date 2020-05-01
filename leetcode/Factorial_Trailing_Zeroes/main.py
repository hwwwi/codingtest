#!/usr/bin/env python3

class Solution:
    def resolve(self, n: int) -> int:
        count = 0

        while(n):
            count += (n//5)
            n = n//5
        return count