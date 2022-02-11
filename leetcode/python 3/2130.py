# 문제 링크: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        reversed_slow = None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = reversed_slow
            reversed_slow = slow
            slow = temp

        max_sum = 0
        while reversed_slow:
            max_sum = max(slow.val + reversed_slow.val, max_sum)
            slow = slow.next
            reversed_slow = reversed_slow.next

        return max_sum
