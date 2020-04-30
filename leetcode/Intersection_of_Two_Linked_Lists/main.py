#!/usr/bin/env python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def resolve(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA = headA
        ptrB = headB
            
        visit = set()
        
        while(ptrA and ptrB):
            if ptrA and (ptrA in visit):
                return ptrA
            else:
                visit.add(ptrA)
                ptrA = ptrA.next
            
            if ptrB and (ptrB in visit):
                return ptrB
            else:
                visit.add(ptrB)
                ptrB = ptrB.next
            
        while(ptrA):
            if ptrA in visit:
                return ptrA
            visit.add(ptrA)
            ptrA = ptrA.next
    
        while(ptrB):
            if ptrB in visit:
                return ptrB
            visit.add(ptrB)
            ptrB = ptrB.next
        return None
