from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    nodes_even = []
    nodes = []
    root = head
    count = 1
    while root:
        if count % 2 == 0:
            nodes_even.append(root)
        else:
            nodes.append(root)
        root = root.next
        count += 1
    nodes.extend(nodes_even)
    if len(nodes) == 0:
        return
    root = head
    for i in range(1, len(nodes)):
        root.next = nodes[i]
        root = nodes[i]
    else:
        root.next = None
    return head


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

b = oddEvenList(a)
while b:
    print(b.val)
    b = b.next