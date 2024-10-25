from collections import defaultdict

def four_sum(nums, target):

    result = set()
    d = defaultdict(lambda:0)
    for i, num in enumerate(nums):
      d[num] += 1
    
    n = len(nums)
    for i in range(n):
      for j in range(i+1, n):
        for k in range(j+1, n):
          rmd = target - nums[i] - nums[j] - nums[k]
          if rmd not in d: continue
          if rmd != nums[i] and rmd != nums[j] and rmd != nums[k]:
            result.add(tuple(sorted([nums[i], nums[j], nums[k], rmd])))
            continue 
          count = 0
          if rmd == nums[i]: count += 1
          if rmd == nums[j]: count += 1
          if rmd == nums[k]: count += 1
          if d[rmd] > count: 
            result.add(tuple(sorted([nums[i], nums[j], nums[k], rmd])))
    return [list(t) for t in result]
