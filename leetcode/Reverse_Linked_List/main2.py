#!/usr/bin/env python3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def resolve(self, head: ListNode) -> ListNode:
        
        prev, curr = None, head
        while(cur):
            curr.next, prev, curr = prev, curr, curr.next
        return prev
