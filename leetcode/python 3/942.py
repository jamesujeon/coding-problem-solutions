# 문제 링크: https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = []
        indexes = [0, len(S)]
        for c in S:
            if c == 'I':
                A.append(indexes[0])
                indexes[0] += 1
            else:
                A.append(indexes[1])
                indexes[1] -= 1
        A.append(indexes[0])
        return A
