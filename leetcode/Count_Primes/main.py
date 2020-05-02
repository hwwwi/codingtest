#!/usr/bin/env python3

class Solution:
    def resolve(self, n:int) -> int:
        sieve = [True] * n

        m = int(n ** 0.5) + 1
        for i in range(2, m):
            if sieve[i]:
                for j in range(i+i, n, i):
                    sieve[j] = False
        return len([x for x in sieve[2:] if x == True])
