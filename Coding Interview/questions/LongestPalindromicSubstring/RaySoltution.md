
def longest_odd_at(s, i):
  ls = len(s)
  for j in range(1, ls):
    if (i-j) < 0 or (i+j) > (ls-1): break 
    if s[i-j] == s[i+j]: continue 
    return s[i-j+1:i+j]
  j = min(i, ls-1-i)
  return s[i-j:i+j+1]
  
def longest_even_at(s, i):
  ls = len(s)
  for j in range(ls-i-1):
    if i -j < 0: break
    if s[i-j] == s[i+1+j]: continue
    return s[i-j+1:i+1+j]
  j = min(i, ls-1-i-1)
  return s[i-j:i+1+j+1]
  
def longest_palindromic_substring(s):
  maxl, maxs = 0, ""
  for i in range(len(s)):
    subs1 = longest_odd_at(s, i)
    if len(subs1) >= maxl:
      maxl = len(subs1)
      maxs = subs1
      
    subs2 = longest_even_at(s, i)
    if len(subs2) >= maxl:
      maxl = len(subs2)
      maxs = subs2 
  return maxs
      
