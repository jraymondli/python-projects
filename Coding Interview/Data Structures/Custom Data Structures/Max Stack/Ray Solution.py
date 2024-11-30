import heapq
from collections import deque

class MaxStack:

    def __init__(self):
      self.stack = deque() 
      self.mstack = deque()

    def push(self, x):
      if len(self.stack) == 0:
        self.stack.append(x)
        self.mstack.append(x)
      else:
        self.stack.append(x)
        self.mstack.append(max(x, self.mstack[-1]))

    def pop(self):
      self.mstack.pop()
      return self.stack.pop()

    def top(self):
      return self.stack[-1]

    def peekMax(self):
      return self.mstack[-1]

    def popMax(self):
        max_e = self.mstack[-1]
        tmp = deque()
        while self.stack and self.stack[-1] != max_e:
          tmp.append(self.stack.pop())
          self.mstack.pop() 
        self.stack.pop()
        self.mstack.pop()
        while tmp:
          self.push(tmp.pop())
        return max_e 
        
          
        
