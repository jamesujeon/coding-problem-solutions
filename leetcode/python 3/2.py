# 문제 링크: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added_number = list(map(int, str(self.extractNumber(l1) + self.extractNumber(l2))))

        root = l = ListNode()
        while added_number:
            l.val = added_number.pop()
            if added_number:
                l.next = ListNode()
                l = l.next

        return root

    def extractNumber(self, l: Optional[ListNode]) -> int:
        number = ''
        while l:
            number = str(l.val) + number
            l = l.next

        return int(number)