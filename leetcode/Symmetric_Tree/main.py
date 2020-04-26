#!/usr/bin/env python3

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def resolve(self, root: TreeNode) -> bool:
        q = deque()
        if root:
            q.appendleft(root)
        while(q):
            size = len(q)
            check = []
            for _ in range(size):
                node = q.pop()
                # print(f"node: {node.val}")
                if node.left:
                    q.appendleft(node.left)
                    check.append(node.left.val)
                    # print(f"left {node.left.val} {check}")
                else:
                    check.append(None)

                if node.right:
                    q.appendleft(node.right)
                    check.append(node.right.val)
                    # print(f"right {node.right.val} {check}")
                else:
                    check.append(None)
            if check != check[::-1]:
                return False
        return True
