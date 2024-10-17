from stack import MainStack
from collections import deque

class MinStack:
    # Initialize min and main stack here
    def __init__(self):
        self.dq = deque()
        self.mdq = deque()

    # Remove and returns value from the stack
    def pop(self):
        self.mdq.pop()
        return self.dq.pop()

    # Pushes values into the stack
    def push(self, value):
        if len(self.dq) == 0:
          self.dq.append(value)
          self.mdq.append(value)
        else:
          self.dq.append(value)
          self.mdq.append(min(value, self.mdq[-1]))

    # Returns minimum value from stack
    def min_number(self):
      return self.mdq[-1]
