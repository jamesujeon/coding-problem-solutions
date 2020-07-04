# 문제 링크: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.right)
            root.val = self.sum = self.sum + root.val
            dfs(root.left)

        dfs(root)
        return root