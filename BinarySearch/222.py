from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


three = TreeNode(1)
three.left = TreeNode(2)
three.right = TreeNode(3)
three.left.left = TreeNode(4)
three.right.left = TreeNode(5)


def countNodes(root: Optional[TreeNode]) -> int:
	if root is None:
		return 0
	return 1 + countNodes(root.left) + countNodes(root.right)

print(countNodes(three))
