#!/usr/bin/env python3
from typing import List

class Solution:
    def resolve(self, nums: List[int], k: int) -> None:
        if k:
            length = len(nums)
            rotate = k - length if k  > length else k

            # print(f"k: {k}, rotate: {rotate}")
            nums[:] = nums[-rotate:] + nums[:length - rotate]
