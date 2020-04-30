#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def resolve(self, head: ListNode) -> bool:
        visit = set()
        ptr = head
        while(ptr):
            # print(f"ptr: {ptr}, visit: {visit}")
            if ptr in visit:
                return True
            visit.add(ptr)
            ptr = ptr.next
        return False
