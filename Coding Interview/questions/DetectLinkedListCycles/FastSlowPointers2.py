from linked_list import LinkedList

def detect_cycle(head):

  p1 = head 
  if p1.next == None: return False
  p1 = p2 = p1.next
  if p2.next == None: return False
  p2 = p2.next
  while p1 and p2:
    if p1 == p2: return True 
    p1 = p1.next
    p2 = p2.next 
    if p2 == None: return False
    p2 = p2.next
  

  return False
