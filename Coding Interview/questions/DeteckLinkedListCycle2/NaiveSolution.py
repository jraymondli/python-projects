from linked_list import LinkedList

def detect_cycle(head):
        
	ns = set()
	curr = head 
	while curr:
	  if curr in ns: return curr
	  ns.add(curr)
	  curr = curr.next 
	  
	return None
