# 문제 링크: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        sums = []
        q = [(1, root)]
        while len(q) > 0:
            level, node = q.pop(0)
            if len(sums) < level:
                sums.append(0)
            sums[level - 1] += node.val

            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

        return sums.index(max(sums)) + 1