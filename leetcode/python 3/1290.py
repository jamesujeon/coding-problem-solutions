# 문제 링크: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def get_binary_value(node: ListNode) -> str:
            if not node:
                return ''
            return f'{node.val}{get_binary_value(node.next)}'

        return int(get_binary_value(head), 2)
