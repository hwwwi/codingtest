#!/usr/bin/env python3
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        if not root:
            return result
        cur = root
        while(cur or stack):
            while(cur):
                stack.append(cur)
                cur = cur.left    
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result
