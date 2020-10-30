# 문제 링크: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(map(str, digits))) + 1))