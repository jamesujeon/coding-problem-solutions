# 문제 링크: https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return (
            self.isIdentical(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def isIdentical(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2

        return (
            root1.val == root2.val and
            self.isIdentical(root1.left, root2.left) and
            self.isIdentical(root1.right, root2.right)
        )
