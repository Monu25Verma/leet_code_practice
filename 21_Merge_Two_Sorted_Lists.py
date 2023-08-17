# Definition for singly-linked list.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(list1, list2):
        head = Node(0, None)
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return head.next


print(Solution.mergeTwoLists(Node(1,Node(2,Node(4, None))), Node(1,Node(3,Node(5, None)))).val)





