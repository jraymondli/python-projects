from collections import defaultdict

def find_sum_of_three(nums, target):
   d = defaultdict(lambda:0)
   for num in nums:
     d[num] += 1
   
   n = len(nums)
   for i in range(n):
     for j in range(n):
       if i == j: continue
       remaining = target - nums[i] - nums[j]
       count = 1
       if remaining == nums[i]: count += 1 
       if remaining == nums[j]: count += 1
       if d[remaining] >= count: return True 
   
   return False
