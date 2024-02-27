from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
	count_path_sum = []

	def get_sum(node: Optional[TreeNode], curr_sum: int):
		if not node:
			if curr_sum == targetSum:
				count_path_sum.append(1)
			return
		get_sum(node.left, curr_sum + node.val)
		get_sum(node.right, curr_sum + node.val)
		if curr_sum == targetSum:
			count_path_sum.append(1)
			return
		if curr_sum > targetSum:
			return

	get_sum(root.left, root.val)

	return len(count_path_sum)


if __name__ == '__main__':
	num = TreeNode(1)
	num.left = TreeNode(2)
	num.right = TreeNode(3)
	# num.left.right = TreeNode(6)
	# num.right.right = TreeNode(5)
	# num.right.right.right = TreeNode(5)
	assert pathSum(num, 3) == 2
