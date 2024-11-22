from heapq import *

class MedianOfStream:
  def __init__(self):
    self.hq1 = []
    self.hq2 = []

  # This function should take a number and store it
  def insert_num(self, num):
    if self.hq1 and (-self.hq1[0]) < (-num):
      heappush(self.hq1, -num)
    elif self.hq2 and num > self.hq2[0]:
      heappush(self.hq2, num)
    else:
      heappush(self.hq1, -num)
    if len(self.hq1) == (len(self.hq2) + 2):
      num2 = - heappop(self.hq1)
      heappush(self.hq2, num2)
    elif len(self.hq2) == (len(self.hq1) + 2):
      num2 = heappop(self.hq2)
      heappush(self.hq1, -num2)    

  # This function should return the median of the stored numbers
  def find_median(self):

    l1, l2 = len(self.hq1), len(self.hq2)
    if l1 > l2: return -self.hq1[0]
    if l2 > l1: return self.hq2[0]
    return (-self.hq1[0] + self.hq2[0]) / 2 
