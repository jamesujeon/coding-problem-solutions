# 문제 링크: https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 and arr[i + 1] % 2 and arr[i + 2] % 2:
                return True
        return False