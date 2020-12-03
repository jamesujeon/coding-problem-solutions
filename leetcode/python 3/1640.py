# 문제 링크: https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            if piece[0] not in arr:
                return False
            index = arr.index(piece[0])
            if arr[index:index + len(piece)] != piece:
                return False
        return True