# 문제 링크: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = current = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                value = l1.val
                l1 = l1.next
            else:
                value = l2.val
                l2 = l2.next
            current.next = ListNode(value)
            current = current.next

        l = l1 or l2
        while l:
            current.next = ListNode(l.val)
            current = current.next
            l = l.next

        root = root.next
        return root