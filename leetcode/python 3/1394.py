# 문제 링크: https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        return max([i for i in set(arr) if i == counts[i]] or [-1])
