# 문제 링크: https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        for i in range(1, target[-1] + 1):
            operations.append('Push')
            if i not in target:
                operations.append('Pop')
        return operations