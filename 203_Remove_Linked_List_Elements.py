# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    pass


class Solution:
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        while head != None and head.val == val:
            head = head.next
        temp = head
        while temp:
            while temp.next and temp.next.val == val:
                temp.next = temp.next.next
            temp = temp.next
        return head

print(Solution.removeElements([1,2,6,3,4,5,6],6))






