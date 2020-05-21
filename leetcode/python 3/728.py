# 문제 링크: https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if sum(d == '0' or i % int(d) for d in str(i)) == 0]
