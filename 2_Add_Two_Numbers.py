# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = n = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)  # divmod  eg---> 5 divisible by 2
            n.next = ListNode(val)
            n = n.next
        return root.next


print(Solution.addTwoNumbers([2,4,3], [5,6,4]))