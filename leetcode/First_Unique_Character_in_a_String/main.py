#!/usr/bin/env python3

class Solution:
    def resolve(self, s: str) -> int:
        check = {}
        for i in s:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        for i in s:
            if check[i] == 1:
                return s.find(i)
        return -1
 