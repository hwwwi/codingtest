#!/usr/bin/env python3

from ..main import Solution
from ..main import TreeNode
import pytest
from typing import List

def create_tree(tree:List[int], root_idx:int) -> TreeNode:
    """
    root_idx: index of root
    level: level
    """
    root = TreeNode(tree[root_idx])
    count = len(tree)
    left = 2*root_idx+1
    right = 2*root_idx+2
    if left < count and tree[left]:
        root.left = create_tree(tree,left)
    if right < count and tree[right]:
        root.right = create_tree(tree,right)
    return root

TEST_CASES = [
    (None, 0),
    (create_tree([3],0),1),
    (create_tree([3,9,None],0),2),
    (create_tree([1,2,2,3,4,4,3],0),3),
    (create_tree([1,2,2,None,3,None,3],0),3),
    (create_tree([3,9,20,None,None,15,7],0),3),
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_resolve(test_input, expected):
    solution = Solution()
    assert solution.resolve(test_input) == expected
