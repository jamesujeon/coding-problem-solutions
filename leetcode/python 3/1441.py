# 문제 링크: https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = []
        operations = []
        for i in range(1, n + 1):
            l.append(i)
            operations.append('Push')
            if l == target:
                break
            if i not in target:
                l.pop()
                operations.append('Pop')
        return operations