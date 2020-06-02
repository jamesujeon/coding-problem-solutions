# 문제 링크: https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        node = TreeNode(root.val)
        left_root = self.increasingBST(root.left)
        if left_root:
            left_leaf = left_root
            while left_leaf.right:
                left_leaf = left_leaf.right
            left_leaf.right = node

        if root.right:
            node.right = self.increasingBST(root.right)

        return left_root if left_root else node