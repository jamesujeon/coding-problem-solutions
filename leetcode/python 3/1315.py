# 문제 링크: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root or (not self.sumParent(root.left) and not self.sumParent(root.right)):
            return 0

        value = 0
        if root.val % 2 == 0:
            value += self.sumParent(root.left)
            value += self.sumParent(root.right)
        value += self.sumEvenGrandparent(root.left)
        value += self.sumEvenGrandparent(root.right)
        return value

    def sumParent(self, root: TreeNode) -> int:
        if not root:
            return 0

        value = 0
        if root.left:
            value += root.left.val
        if root.right:
            value += root.right.val
        return value