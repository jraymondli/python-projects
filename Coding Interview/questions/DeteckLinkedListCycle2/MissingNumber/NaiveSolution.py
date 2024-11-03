def find_disappeared_numbers(nums):
    n = len(nums)
    s = set()
    for num in nums:
      s.add(num)
      
    res = []
    for i in range(1, n+1):
      if i not in s:
        res.append(i)
    return res
