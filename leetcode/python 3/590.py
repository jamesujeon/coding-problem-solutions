# 문제 링크: https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        tree = []
        if root.children:
            for child in root.children:
                tree += self.postorder(child)
        tree += [root.val]
        return tree
