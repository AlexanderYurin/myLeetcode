class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def goodNodes(root: TreeNode) -> int:
	def good_node(max_value, node):
		if not node:
			return 0
		val = node.val
		if val >= max_value:
			return 1 + good_node(val, node.left) + good_node(val, node.right)
		return 0 + good_node(max_value, node.left) + good_node(max_value, node.right)
	return 1 + good_node(root.val, root.left) + good_node(root.val, root.right)


if __name__ == '__main__':
	num = TreeNode(9)
	num.left = TreeNode(3)
	# num.left.left = TreeNode(3)
	num.left.right = TreeNode(6)
	# num.right.right = TreeNode(5)
	# num.right.right.right = TreeNode(5)

	assert goodNodes(num) == 1
