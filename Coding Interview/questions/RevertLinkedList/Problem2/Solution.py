from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list
  
def findMarkers(head, left, right):
  left_prev, right_next = None, None 

  prev, curr = head, head.next 
  pos = 2
  while curr:
    if pos == left: left_prev = prev 
    if pos == right: right_next = curr.next 
    prev = curr 
    curr = curr.next 
    pos += 1
  return left_prev, right_next
    
def reverse_between(head, left, right):
  if head == None or head.next == None or left == right: return head 
  
  left_prev, right_next = findMarkers(head, left, right)
  # print(left_prev.data, right_next.data)
  if left_prev == None: prev = head
  else: prev = left_prev.next 
  curr, new_tail = prev.next, right_next
  while curr != right_next: 
    next = curr.next 
    prev.next = new_tail 
    new_tail = prev  
    prev = curr 
    curr = next 
  prev.next = new_tail
  if left_prev == None: return prev
  left_prev.next = prev 
  return head
