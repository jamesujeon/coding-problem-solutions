# 문제 링크: https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Get the last node of the list2
        list2_last_node = list2
        while list2_last_node.next:
            list2_last_node = list2_last_node.next

        node = list1
        for i in range(b + 1):
            next_node = node.next
            # Connect the previous node of the a-th node to the list2
            if i == a - 1:
                node.next = list2
            node = next_node
        # Connect the last node of the list2 to the b-th node
        list2_last_node.next = node

        return list1