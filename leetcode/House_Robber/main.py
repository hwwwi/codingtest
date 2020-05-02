#!/usr/bin/env python3

from typing import List

class Solution:
    def getNum(self, nums:List[int], dp:List[int], idx:int) -> int:
        if idx >= len(nums):
            return 0
        if dp[idx] != -1:
            return dp[idx]
        dp[idx] = max(self.getNum(nums, dp, idx+1), nums[idx] + self.getNum(nums,dp, idx+2))
        return dp[idx]

    def resolve(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.getNum(nums, dp, 0)
