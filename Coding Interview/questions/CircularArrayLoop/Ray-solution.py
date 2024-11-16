def getNext(nums, i):
  n = len(nums)
  nxt = i + nums[i]
  if nxt >= n: nxt = nxt % n
  if nxt < 0: nxt = nxt % n
  return nxt 

def check(nums, i):
  if nums[i] > 0: dir = 1
  else: dir = -1
  
  fast = slow = i 
  
  while True:
    fast = getNext(nums, getNext(nums, fast))
    slow = getNext(nums, slow)
    if (nums[slow] * dir)  < 0: return False 
    if (nums[fast] * dir) < 0: return False
    if fast == slow: 
      if getNext(nums, fast) == fast: return False
      return True 
  
  
def circular_array_loop(nums):  

    for i in range(len(nums)):
      if check(nums, i): return True
    return False
