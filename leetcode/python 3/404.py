# 문제 링크: https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def sum_leaves(root: TreeNode, is_left: bool) -> int:
            if not root:
                return 0
            if not root.left and not root.right and is_left:
                return root.val
            return sum_leaves(root.left, True) + sum_leaves(root.right, False)

        return sum_leaves(root, False)