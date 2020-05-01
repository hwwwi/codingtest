#!/usr/bin/env python3

class Solution:
    def resolve(self, s: str) -> int:
        pos = 0
        result = 0
        for ch in s[::-1]:
            result += ((26**pos) * (ord(ch)-64))
            pos += 1
        return result