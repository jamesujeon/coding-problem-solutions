# 문제 링크: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        count = int(len(arr) * 0.05)
        arr = sorted(arr)[count:-count]
        return sum(arr) / len(arr)