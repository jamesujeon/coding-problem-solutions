# 문제 링크: https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k < 0:
            return self.decrypt(code[::-1], -k)[::-1]

        l = len(code)
        return [sum(code[j % l] for j in range(i, i + k)) for i in range(1, l + 1)]