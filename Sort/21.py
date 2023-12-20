from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	result = ListNode()

	while 1:
		if list1.val < list2.val:
			




	return result


if __name__ == '__main__':
	list1 = ListNode(1, 2)
	list1.val = ListNode(2, 3)
	list1.next.val = ListNode(3)
	list2 = ListNode(1, 2)
	list2.val = ListNode(2, 3)
	list2.next.val = ListNode(3)
	assert type(mergeTwoLists(list1, list2)) == ListNode
