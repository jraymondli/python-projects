from collections import deque

def updateBuf(nums, dq, i):
    while dq:
      if nums[i] > nums[dq[-1]]:
        dq.pop()
      else: break
    dq.append(i) 
    
def find_max_sliding_window(nums, w):
  dq = deque()
  dq.append(0)
  for i in range(1, w):
    updateBuf(nums, dq, i)
    
  result = []
  n = len(nums)
  for i in range(0, n-w+1):
    print(dq)
    result.append(nums[dq[0]])
    if dq[0] == i: dq.popleft()
    if i != (n-w):
      updateBuf(nums, dq, i+w)
      
  return result    
    
