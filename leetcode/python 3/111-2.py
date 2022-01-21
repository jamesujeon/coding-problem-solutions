# 문제 링크: https://leetcode.com/problems/minimum-depth-of-binary-tree/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue

            if not node.left and not node.right:
                return depth
            else:
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return 0