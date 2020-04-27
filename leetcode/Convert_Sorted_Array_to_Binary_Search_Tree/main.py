#!/usr/bin/env python3

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def resolve(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.resolve(nums[:mid])
        root.right = self.resolve(nums[mid+1:])
        return root
