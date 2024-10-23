from linked_list import *
from linked_list_node import *

def find_middle(head):
  fast = slow = head 
  prev = head 
  while fast and fast.next:
    fast = fast.next 
    fast = fast.next 
    prev = slow
    slow = slow.next 
  prev.next = None 
  return slow 
  
def merge_two_sorted_lists(l1, l2):
  if l1 == None: return l2
  if l2 == None: return l1
  if l1.data <= l2.data: 
    head = l1 
    curr = l1
    l1 = l1.next
  else: 
    head = l2
    curr = l2 
    l2 = l2.next
  while l1 and l2: 
    if l1.data < l2.data:
      curr.next = l1
      l1 = l1.next 
    else:
      curr.next = l2
      l2 = l2.next 
    curr = curr.next 
  while l1:
    curr.next = l1
    l1 = l1.next
    curr = curr.next
  while l2:
    curr.next = l2
    l2 = l2.next
    curr = curr.next
  return head
    

def sort_list(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    left = sort_list(head)
    right = sort_list(mid)
    
    return merge_two_sorted_lists(left, right)
