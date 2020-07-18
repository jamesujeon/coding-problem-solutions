# 문제 링크: https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        parts, start, end = [], -1, 0
        for i in range(len(S)):
            end = max(end, S.rfind(S[i]))
            if i == end:
                parts.append(end - start)
                start = end
        return parts