# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merge_list = ListNode()
    root = merge_list
    while list1 and list2:
        if list1.val <= list2.val:
            merge_list.next = list1
            list1 = list1.next

        else:
            merge_list.next = list2
            list2 = list2.next
        merge_list = merge_list.next

    if list1:
        merge_list.next = list1
    else:
        merge_list.next = list2

    return root.next


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    root = mergeTwoLists(list1, list2)
    while root:
        print(root.val)
        root = root.next

