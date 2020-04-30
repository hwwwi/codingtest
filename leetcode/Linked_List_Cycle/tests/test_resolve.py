#!/usr/bin/env python3

from ..main import Solution, ListNode
from ..main2 import Solution as Solution2
from ..main3 import Solution as Solution3
import pytest


TEST_CASES = [
    ([3,2,0,-4],1,True),
    ([1,2],0,True),
    ([1],-1, False),
    ([1,2,3,4,5,6],-1, False)
]

def create_list(node, pos):
    list_node = ListNode(None)
    ptr = list_node
    idx = 0
    for i in node:
        n = ListNode(i)
        ptr.next = n
        ptr = ptr.next
        if idx == pos:
            cycle_node = n
        idx += 1
    if pos != -1:
        ptr.next = cycle_node
    return list_node.next

@pytest.mark.parametrize("node, pos, expected", TEST_CASES)
def test_resolve(node, pos, expected):
    solution = Solution()
    assert solution.resolve(create_list(node, pos)) == expected

@pytest.mark.parametrize("node, pos, expected", TEST_CASES)
def test_resolve2(node, pos, expected):
    solution = Solution2()
    assert solution.resolve(create_list(node, pos)) == expected

@pytest.mark.parametrize("node, pos, expected", TEST_CASES)
def test_resolve2(node, pos, expected):
    solution = Solution3()
    assert solution.resolve(create_list(node, pos)) == expected