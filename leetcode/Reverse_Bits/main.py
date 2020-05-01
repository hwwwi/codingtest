#!/usr/bin/env python3

class Solution:
    def resolve(self, n: int) -> int:
        b = bin(n)[:1:-1]
        return int(b + '0'*(32-len(b)), base=2)