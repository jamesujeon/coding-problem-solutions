# 문제 링크: https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        def dfs(node: TreeNode) -> bool:
            if not node:
                return True
            return node.val == value and dfs(node.left) and dfs(node.right)
        return dfs(root)