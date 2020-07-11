# 문제 링크: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, bits: str) -> int:
            if not node:
                return 0
            bits += str(node.val)
            if not node.left and not node.right:
                return int(bits, 2)
            return dfs(node.left, bits) + dfs(node.right, bits)

        return dfs(root, '')
