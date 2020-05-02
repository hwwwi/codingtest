#!/usr/bin/env python3

class Solution:
    def resolve(self, a: int, b: int) -> int:
        def add(a,b):
            while b:
                c = a&b
                a = a^b
                b = c<<1
            return a
            
        def subtract(a,b):
            while b:
                bor = ~a&b
                a = a^b
                b=bor<<1
            return a
        a,b = min(a,b), max(a,b)
        if a<0 and b<0:
            return add(a,b)
        if a<0:
            if -a>b:
                return -1*subtract(-a,b)
            else:
                return subtract(b,-a)
        return add(a,b)