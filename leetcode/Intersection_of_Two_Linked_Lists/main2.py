#!/usr/bin/env python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def resolve(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None or headB == None):
            return None
        
        ptrA = headA
        ptrB = headB
        
        while(ptrA or ptrB):
            if not ptrA:
                ptrA = headB
            if not ptrB:
                ptrB = headA
            if ptrA == ptrB:
                return ptrA      
            ptrA = ptrA.next
            ptrB = ptrB.next
            
        return None
