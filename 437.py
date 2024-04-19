from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
	counts = []
	def get_sum(node: Optional[TreeNode], curr_sum: int = 0):
		if not node:
			return
		curr_sum += node.val
		if curr_sum == targetSum:
			counts.append(1)

		return get_sum(node.left, curr_sum) or get_sum(node.right, curr_sum)

	if not root:
		return len(counts)

	get_sum(root)

	# if root.val == targetSum:
	# 	count += 1




	return len(counts) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)


if __name__ == '__main__':
	num = TreeNode(1)
	num.left = TreeNode(-2)
	num.right = TreeNode(-3)
	num.left.right = TreeNode(3)
	num.left.left = TreeNode(1)
	num.right.left = TreeNode(-2)
	num.left.left.left = TreeNode(-1)
	# num.left.left.right = TreeNode(-2)
	# num.left.right.right = TreeNode(1)
	num1 = TreeNode(1)
	assert pathSum(num, -1) == 4
	assert pathSum(num1, 1) == 1, f"{pathSum(num1, 1)}"

