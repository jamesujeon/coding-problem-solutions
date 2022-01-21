# 문제 링크: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth and right_depth:
            return min(left_depth, right_depth) + 1
        else:
            return (left_depth or right_depth) + 1