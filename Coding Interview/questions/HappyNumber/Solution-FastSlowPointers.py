
def proc(n):
  r = 0
  while n:
    r += (n%10) **2 
    n = n//10
  return r 
  
def is_happy_number(n):

  n1 = n2 = n
  while True:
    n1 = proc(n1)
    if n1 == 1: return True
    n2 = proc(proc(n2))
    if n1 == n2: return False
    
