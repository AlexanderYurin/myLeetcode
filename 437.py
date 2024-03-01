from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
	def get_sum(node: Optional[TreeNode], curr_sum: int = 0):
		if not node:
			return 0
		curr_sum += node.val
		if curr_sum == targetSum:
			return 1
		if curr_sum > targetSum:
			return 0
		return get_sum(node.left, curr_sum) + get_sum(node.right, curr_sum)

	if not root:
		return 0
	left = get_sum(root.left, root.val)
	right = get_sum(root.right, root.val)
	count = 0
	if root.val == targetSum:
		count = 1
	return count + left + right + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)


if __name__ == '__main__':
	num = TreeNode(10)
	num.left = TreeNode(5)
	num.right = TreeNode(-3)
	num.left.right = TreeNode(2)
	num.left.left = TreeNode(3)
	num.right.right = TreeNode(11)
	num.left.left.left = TreeNode(3)
	num.left.left.right = TreeNode(-2)
	num.left.right.right = TreeNode(1)
	num1 = TreeNode(1)
	assert pathSum(num, 8) == 3
	assert pathSum(num1, 1) == 1, f"{pathSum(num1, 1)}"

