from linked_list import LinkedList

def detect_cycle(head):
    if not head or not head.next:
        return None

    # 1. detect the cycke
    fast, slow = head, head
    while fast and fast.next:
      slow = slow.next 
      fast = fast.next.next
      if slow == fast:
        break 
      
    if fast == None or fast.next == None:
      return None 
      
    # 2. find the start of the cycle 
    slow = head 
    while slow != fast:
      slow = slow.next 
      fast = fast.next 
    return fast 
