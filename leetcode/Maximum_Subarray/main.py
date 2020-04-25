#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self, nums: List[int]) -> int:
        #  contiguous subarray (containing at least one number)
        #  which has the largest sum and return its sum

        dp = [0] * len(nums) # dp[i] is maximum sum of value until index i
        dp[0] = nums[0]
        for idx, val in enumerate(nums[1:], 1):
            dp[idx] = max(val, val + dp[idx-1])
        return max(dp)