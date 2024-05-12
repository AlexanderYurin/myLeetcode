import dataclasses
from typing import Optional
@dataclasses.dataclass
class ListNode:
    val:int = 0
    next= None




def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Основная идея в сохранение предыдущей ссылки чтобы не было потери значения
    """
    if not head or not head.next:
        return head

    n1, n2, new_head, prev= head, head.next, head.next, None


    while n2:
        if prev:
            prev.next = n2



        n2.next, n1.next = n1, n2.next

        if not n1.next:
            break
        prev = n1
        n1 = n1.next
        n2 = n1.next

    return new_head



if __name__ == '__main__':
    a = ListNode(1)
    r = a
    c = 2

    while c != 5:
        a.next = ListNode(c)
        a = a.next
        c += 1

    roots = swapPairs(r)

    while roots:
        print(roots.val)
        roots = roots.next
