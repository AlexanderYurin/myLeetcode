from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
	def get_sum(node: Optional[TreeNode], curr_sum: int = 0):
		if not node or curr_sum > targetSum:
			return 0
		if curr_sum == targetSum:
			return 1
		return get_sum(node.left, curr_sum + node.val) + get_sum(node.right, curr_sum + node.val)

	if not root:
		count = 0
		return count
	count = get_sum(root)

	return count + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)


if __name__ == '__main__':
	num = TreeNode(1)
	num.left = TreeNode(2)
	num.right = TreeNode(3)
	# num.left.right = TreeNode(6)
	# num.right.right = TreeNode(5)
	# num.right.right.right = TreeNode(5)
	print(pathSum(num, 3))
	assert pathSum(num, 3) == 2
