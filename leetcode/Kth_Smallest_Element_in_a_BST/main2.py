#!/usr/bin/env python3

import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def resolve(self, root: TreeNode, k: int) -> int: 
        mst = []
        def tree_to_list(tree: TreeNode):
            if tree:
                mst.append(tree.val)
                if tree.left:
                    tree_to_list(tree.left)
                if tree.right:
                    tree_to_list(tree.right)
        tree_to_list(root)

        return sorted(mst)[k-1]


        

