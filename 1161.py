from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def maxLevelSumroot(root: Optional[TreeNode]) -> int:
	if not root:
		return []
	stack = [root]
	level = 0
	max_sum = float("-inf")
	count = 1
	while stack:
		cur_sum = sum(map(lambda x: x.val, stack))
		if cur_sum > max_sum:
			max_sum = cur_sum
			level = count
		nodes = []
		for node in stack:
			if node.left:
				nodes.append(node.left)
			if node.right:
				nodes.append(node.right)
		stack = nodes[:]
		nodes.clear()
		count += 1
	return level
