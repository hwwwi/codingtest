#!/usr/bin/env python3

class Solution:
    def resolve(self, n:int) -> int:
        # 1, 2 
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(n+1)[3::]:
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]