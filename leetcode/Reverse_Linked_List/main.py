#!/usr/bin/env python3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def resolve(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None): 
            return head
        p = self.resolve(head.next)
        head.next.next = head
        head.next = None
        return p
