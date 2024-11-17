from linked_list import LinkedList
from linked_list_node import LinkedListNode

def breakList(head):
  fast = slow = head 
  prev = None
  while fast and fast.next:
    fast = fast.next.next 
    prev = slow
    slow = slow.next 
  if fast: prev, slow = slow, slow.next 
  prev.next = None
  return slow 
  
def printList(head):
  vals = []
  curr = head 
  while curr:
    vals.append(curr.data)
    curr = curr.next 
  print(vals)
  
def revertList(head):
  if head == None or head.next == None: return head 
  prev, curr, new_tail = head, head.next, None
  while curr:
    prev.next = new_tail
    new_tail = prev 
    prev = curr 
    curr = curr.next 
  prev.next = new_tail 
  return prev 

def mergeList(head, h2):
  ptr1 = head 
  ptr2 = h2 
  while ptr1 and ptr2: 
    nxt1, nxt2 = ptr1.next, ptr2.next
    ptr1.next = ptr2 
    ptr2.next = nxt1 
    ptr1, ptr2 = nxt1, nxt2 
  return head 
            
def reorder_list(head):

    h2 = breakList(head)
    head2 = revertList(h2)
    mergeList(head, head2)
    return head
