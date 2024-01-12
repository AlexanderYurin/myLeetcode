# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
	def get_nums(l1: Optional[ListNode]) -> List[int]:
		if not l1:
			return []
		return [str(l1.val)] + get_nums(l1.next)

	def get_list_node(l: List[int]) -> Optional[ListNode]:
		root = ListNode(int(l.pop()))
		node = root
		while l:
			node.next = ListNode(int(l.pop()))
			node = node.next
		return root

	nums_1 = int("".join(reversed(get_nums(l1))))
	nums_2 = int("".join(reversed(get_nums(l2))))
	result = list(str(nums_1 + nums_2))

	return get_list_node(result)
