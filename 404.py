from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    count = 0
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        count = root.left.val
    return count + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

