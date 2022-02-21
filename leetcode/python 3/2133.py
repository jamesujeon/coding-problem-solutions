# 문제 링크: https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(len(set(nums)) == len(nums) for nums in matrix + list(zip(*matrix)))
