from heapq import heappush, heappop
from collections import defaultdict

def median_sliding_window(nums, k):

    hq_small, hq_larg = [], [] 
    outgoing_d = defaultdict(lambda:0)
    for i in range(k): 
      heappush(hq_larg, nums[i])
    for i in range(k//2): heappush(hq_small, -heappop(hq_larg))
    result = []
    for i in range(len(nums) + 1 -k):
      if k % 2 == 1: 
        result.append(hq_larg[0])
      else:
        result.append(hq_larg[0]/2 - hq_small[0]/2)
      if i == (len(nums) -k): break
      
      incoming, outgoing = nums[i+k], nums[i]
      
      balance = 0
      if outgoing >= hq_larg[0]:
        balance += 1 
      else: 
        balance -= 1
      outgoing_d[outgoing] += 1 
      
      if hq_small == [] or incoming < - hq_small[0]:
        heappush(hq_small, -incoming)
        balance += 1
      else:
        heappush(hq_larg, incoming)
        balance -= 1 
        
      if balance < 0:
        heappush(hq_small, -heappop(hq_larg))
      elif balance > 0:
        heappush(hq_larg, - heappop(hq_small))
      balance = 0
            
      while hq_small and -hq_small[0] in outgoing_d and outgoing_d[-hq_small[0]] > 0: 
        outgoing_d[-hq_small[0]] -= 1 
        heappop(hq_small)

      while hq_larg[0] in outgoing_d and outgoing_d[hq_larg[0]] > 0:
        outgoing_d[hq_larg[0]]  -= 1
        heappop(hq_larg)
    
    return result
  
