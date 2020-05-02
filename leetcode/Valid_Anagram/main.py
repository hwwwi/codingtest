#!/usr/bin/env python3

class Solution:
    def resolve(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
