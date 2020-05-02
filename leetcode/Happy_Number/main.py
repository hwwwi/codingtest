#!/usr/bin/env python3

class Solution:
    def resolve(self, n:int) -> bool:
        check = set()
        check.add(n)
        next_num = n
        while(True):
            temp = next_num
            calc_num = 0
            while(temp):
                temp, r = divmod(temp, 10)
                calc_num += r**2
            if calc_num == 1:
                return True
            if calc_num in check:
                return False
            check.add(calc_num)
            next_num = calc_num