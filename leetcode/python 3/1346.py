# 문제 링크: https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True

        s = set(arr)
        s.discard(0)
        return any(num * 2 in s for num in arr)