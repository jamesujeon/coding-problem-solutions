# 문제 링크: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        for _ in range(count // 2):
            head = head.next
        return head