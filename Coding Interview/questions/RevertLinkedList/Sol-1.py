class ListNode:
    def __init__(self, val: int, nxt=None) -> None:
        self.val = val
        self.next = nxt

tail = ListNode(5, None)
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, tail))))

def revert(head: ListNode, tail: ListNode):
    if head == tail: return head

    tail.next = None

    prev = head
    curr = head.next
    head.next = None
    
    new_tail = None

    while curr:
       
        prev.next = new_tail
        new_tail = prev

        prev = curr
        curr = curr.next

    prev.next = new_tail

    return prev, head

new_head = revert(l, tail)

curr, new_tail = new_head
while curr:
    print(curr.val)
    curr = curr.next 
