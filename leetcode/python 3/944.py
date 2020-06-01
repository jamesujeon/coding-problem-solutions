# 문제 링크: https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(list(column) != sorted(column) for column in zip(*A))