from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    root = head #2
    swap_node = None #1

    head = head.next
    root.next = head.next
    head.next = root

    return head
    # c = 0
    #
    # while root:
    #     if c % 2 != 0:
    #         swap_node = root
    #         root = root.next
    #     else:
    #         a = root.next
    #         print(a.val)
    #         b = swap_node
    #         print(b.val)
    #         swap_node = root
    #
    #
    #
    #     c += 1
    # return head


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    # a.next.next = ListNode(3)
    # a.next.next.next = ListNode(4)

    roots = swapPairs(a)

    while roots:
        print(roots.val)
        roots = roots.next
