#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



"""
    if (head == null || head.next == null) {
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    while (slow != fast) {
        if (fast == null || fast.next == null) {
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
"""
class Solution:
    def resolve(self, head: ListNode) -> bool:
        if (head == None or head.next == None):
            return False;
        slow = head
        fast = head.next
        while(slow != fast):
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True