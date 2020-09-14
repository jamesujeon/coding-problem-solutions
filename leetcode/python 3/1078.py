# 문제 링크: https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        answer = []
        for i in range(len(text) - 2):
            if text[i] != first or text[i + 1] != second:
                continue
            answer.append(text[i + 2])
        return answer