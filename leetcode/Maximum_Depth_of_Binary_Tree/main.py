#!/usr/bin/env python3

from collections import deque
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def resolve(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)        
        depth = 0
        while(q):
            depth += 1
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth


        
