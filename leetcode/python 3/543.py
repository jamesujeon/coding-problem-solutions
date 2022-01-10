# 문제 링크: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            self.diameter = max(left_height + right_height, self.diameter)
            return max(left_height, right_height) + 1

        get_height(root)

        return self.diameter