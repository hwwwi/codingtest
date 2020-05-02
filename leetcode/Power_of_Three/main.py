#!/usr/bin/env python3

class Solution:
    def resolve(self, n:int):
        if n == 1:
            return True
        if n < 3:
            return False
        while(n >= 3):
            a,b = divmod(n,3)
            # print(f"a:{a}, b:{b}")
            if b:
                return False
            n = a
        return b == 0 and a <= 1