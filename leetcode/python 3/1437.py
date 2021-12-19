# 문제 링크: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums or k == 0:
            return True

        prev = nums.index(1)
        for i in range(prev + 1, len(nums)):
            if nums[i] == 0:
                continue

            if i - prev <= k:
                return False

            prev = i

        return True