# 문제 링크: https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        answer = []
        for letter in A.pop(0):
            if all(letter in a_str for a_str in A):
                for i in range(len(A)):
                    A[i] = A[i].replace(letter, '', 1)
                answer.append(letter)
        return answer