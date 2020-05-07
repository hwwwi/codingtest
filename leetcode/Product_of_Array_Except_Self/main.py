#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self,nums: List[int]) -> List[int]:
        
        length = len(nums)
        num_of_zero = nums.count(0)
        if num_of_zero >= 2:
            return [0] * length
        else:
            product_all = 1
            for num in nums:
                if num != 0:
                    product_all *= num
            if num_of_zero == 1:
                res = [0] * length
                res[nums.index(0)] = product_all
            else:
                res = [product_all//num for num in nums]
        return res