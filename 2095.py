# Definition for singly-linked list.
from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
	links = []
	root = head
	while root:
		links.append(root)
		root = root.next
	if len(links) < 2:
		return
	if len(links) == 2:
		return ListNode(head.val)
	mid = len(links) // 2
	root = head
	for i in range(1, len(links)):
		if i != mid:
			root.next = links[i]
			root = links[i]
	return head
