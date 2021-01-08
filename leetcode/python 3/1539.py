# 문제 링크: https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count, i, num = 0, 0, 1
        while i < len(arr):
            if arr[i] == num:
                i += 1
            else:
                count += 1
                if count == k:
                    return num
            num += 1

        return arr[-1] + k - count