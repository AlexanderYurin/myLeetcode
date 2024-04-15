# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

    def _addOneRow(root, curr_depht=2):
        if curr_depht == depth:
            left = TreeNode(val=val, left=root.left, right=root.right)
            right = TreeNode(val=val, left=root.left, right=root.right)
            root.left = left
            root.right = right
            return
        if not root:
            return
        _addOneRow(root.left, curr_depht+1)
        _addOneRow(root.right, curr_depht+1)

    _addOneRow(root)

    return root


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)


addOneRow(a, 4, 2)


nodes = [a]
values = []
for node in nodes:
    if node:
        values.append(node.val)
        nodes.append(node.left)
        nodes.append(node.right)

print(values)

