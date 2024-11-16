from linked_list import LinkedList
from linked_list_node import LinkedListNode

def remove_nth_last_node(head, n):
    
    nl = 0 
    curr = head
    while curr:
      nl += 1
      curr = curr.next 
      
    if n > nl: return None
  
    if n == nl: return head.next 
    
    prev = head 
    curr = head.next 
    for i in range(nl-n-1):
      prev = curr
      curr = curr.next 
      
    prev.next = curr.next 
    return head 
  
  
