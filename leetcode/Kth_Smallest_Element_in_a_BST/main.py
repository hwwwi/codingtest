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
        def sort_tree(tree: TreeNode) -> None:
            if tree:
                mst.append(tree.val)
                if tree.left and tree.left.val < tree.val:
                    tree.val, tree.left.val = tree.left.val, tree.val
                    sort_tree(tree.left)
                if tree.right and tree.right.val < tree.val:
                    tree.val, tree.right.val = tree.right.val, tree.val
                    sort_tree(tree.right)
        
        def find_min(n: int) -> int:
            
        sort_tree(root) 

        return sorted(mst)[k-1]


        

