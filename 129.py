# Definition for a binary tree node.
from functools import reduce
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def sumNumbers(root: Optional[TreeNode]) -> int:
    nums = []

    def get_nums(root, num=""):
        if root and not root.left and not root.right:
            return nums.append(int(num + str(root.val)))
        if root.left:
            get_nums(root.left, num + str(root.val))
        if root.right:
            get_nums(root.right, num + str(root.val))
    get_nums(root)
    return sum(nums)


a = TreeNode(1)
# a.left = TreeNode(2)
a.right = TreeNode(3)
# a.left.right = TreeNode(2)
# a.left.left = TreeNode(2)

print(sumNumbers(a))