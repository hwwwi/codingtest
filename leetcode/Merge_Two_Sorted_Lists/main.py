#!/usr/bin/env python3

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:        
        if not (l1 and l2):
            return l1 or l2
        
        result = ListNode(None)
        pr = result
        p1 = l1
        p2 = l2
        while (p1 and p2):
            if p1.val < p2.val:
                pr.next = ListNode(p1.val)
                pr = pr.next
                p1 = p1.next
            else:
                pr.next = ListNode(p2.val)
                pr = pr.next
                p2 = p2.next
        while(p1):
            pr.next = ListNode(p1.val)
            pr = pr.next
            p1 = p1.next
        while(p2):
            pr.next = ListNode(p2.val)
            pr = pr.next
            p2 = p2.next
        return result.next    

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    result = Solution().mergeTwoLists(l1, l2)
    temp = result
    while(temp):
        print(temp.val)
        temp = temp.next
   
    
    