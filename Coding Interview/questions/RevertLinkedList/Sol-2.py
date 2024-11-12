class ListNode:
    def __init__(self, val: int, nxt=None) -> None:
        self.val = val
        self.next = nxt

tail = ListNode(5, None)
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, tail))))

def revert(head: ListNode, tail: ListNode):
    if head == None: return head 
    if head == tail: return tail 
    new_tail = head
    curr = head.next 
    head.next = None
    while curr:
        nxt = curr.next 
        curr.next = new_tail
        new_tail = curr 
        curr = nxt

    return tail 

def printList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next 

printList(l)
new_head = revert(l, tail)
printList(new_head)


## Key take away in pointer manipulation is to save pointer (which is needed later in a different calculation) before modifying it




