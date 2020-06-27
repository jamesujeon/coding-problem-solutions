# 문제 링크: https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        leaf_values = {}
        def get_leaf_values(root: TreeNode, depth: int):
            if not root:
                return

            if not root.left and not root.right:
                if depth not in leaf_values:
                    leaf_values[depth] = []
                leaf_values[depth].append(root.val)
                return

            get_leaf_values(root.left, depth + 1)
            get_leaf_values(root.right, depth + 1)

        get_leaf_values(root, 0)
        return sum(leaf_values[max(leaf_values.keys())])