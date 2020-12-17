# 문제 링크: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(
            ((i + 1) * (len(arr) - i) + 1) // 2 * num 
            for i, num in enumerate(arr)
        )