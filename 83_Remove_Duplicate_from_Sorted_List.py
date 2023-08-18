# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    pass


class Solution:
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


print(Solution.deleteDuplicates([1, 1, 2, 3, 3]))
