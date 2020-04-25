#!/usr/bin/env python3

class Solution:
    def resolve(self, x:int) -> int:
        if x == 0 or x == 1:
            return x
        start = 1
        end = int(x/2)

        while(start<=end):
            mid = int((start+end)/2)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        return end if end * end <= x else start