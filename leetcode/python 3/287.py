# 문제 링크: https://leetcode.com/problems/find-the-duplicate-number/

# 플로이드 순환 찾기 알고리즘 (Floyd's cycle-finding algorithm)
# https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow