
def xor_sum(nums):
  r = 0 
  for num in nums:
    r = r ^ num 
  return r 
  
def get_differ_bit(s):
  # get the right most differ bit 
  i = 0 
  while True: 
    if (1 << i) & s: return i 
    i += 1 
    
def two_single_numbers(arr):

  s = xor_sum(arr)
  b = get_differ_bit(s)
  s1 = 0
  print(b)
  for num in arr:
    if num & (1 << b): s1 = s1 ^ num 
  return [s1, s ^ s1]
  
  
