# 문제 링크: https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        tree_str = str(root.val)
        if root.left:
            tree_str += '(' + self.tree2str(root.left) + ')'
        if root.right:
            if not root.left:
                tree_str += '()'
            tree_str += '(' + self.tree2str(root.right) + ')'

        return tree_str
