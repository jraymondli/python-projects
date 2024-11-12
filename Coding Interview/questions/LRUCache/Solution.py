from linked_list import LinkedList

# Tip: You may use some of the code templates provided
# in the support files

# We will use a linkedlist of a pair of integers
# where the first integer will be the key
# and the second integer will be the value

class ListNode:
  def __init__(self, key, prev=None, next=None):
    self.key = key 
    self.prev = prev
    self.next = next


class LRUCache:
    def __init__(self, capacity):
      self.capacity = capacity
      self.ln_dict = {}
      self.val_dict = {}
      self.head = None 
      self.tail = None
      
    def update(self, key):
        ln = self.ln_dict[key]
        if ln != self.head: 
            if ln == self.tail:
              self.tail = ln.prev 
            ln.prev.next = ln.next 
            if ln.next: ln.next.prev = ln.prev 
            ln.prev = None 
            ln.next = self.head 
            self.head.prev = ln
            self.head = ln

    def get(self, key):
        if key not in self.val_dict: return -1
        rv = self.val_dict[key]
        self.update(key)
        return rv

    def set(self, key, value):
        if len(self.val_dict) == self.capacity:
          d_key = self.tail.key
          if self.capacity == 1:
            self.prev = self.tail = None 
          else:
            prev = self.tail.prev
            prev.next = None 
            self.tail.prev = None 
            self.tail = prev 
          del self.ln_dict[d_key]
          del self.val_dict[d_key]
        if key not in self.val_dict:
          self.val_dict[key] = value
          ln = ListNode(key)
          self.ln_dict[key] = ln 
          ln.next = self.head 
          if self.head: self.head.prev = ln 
          self.head = ln 
          if self.tail == None: self.tail = ln
        else:
          self.val_dict[key] = value
          self.update(key)
        
          
        
