#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:list) -> ListNode:
        if not (l1 and l2):
            return l1 or l2
        
        result = ListNode(None)
        p1 = l1 # pivot1
        p2 = l2 # pivot2
        pr = result # pivot result
        carry = 0

        while(p1 or p2 or carry): 
            if p1:
               p1_val = p1.val
               p1 = p1.next
            else:
                p1_val = 0 
            if p2:
                p2_val = p2.val
                p2 = p2.next
            else:
                p2_val = 0
            # print(f"carry= {carry}")
            # print(f"p1.val= {p1_val}")
            # print(f"p2.val= {p2_val}")
            # print(f"sum_of_val= {sum_of_val}")
            carry, r_val = divmod(carry + p1_val + p2_val, 10)
            pr.next = ListNode(r_val)
            pr = pr.next
        return result.next
        

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(8)
    l1.next.next.next = ListNode(9)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    temp = result
    while(temp):
        print(temp.val)
        temp = temp.next