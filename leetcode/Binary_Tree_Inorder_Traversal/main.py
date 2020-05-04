#!/usr/bin/env python3
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            if node.left:
                inorder(node.left)
            result.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return result
