
def rescue_boats(people, limit):

  people.sort()
  l, r, count = 0, len(people)-1, 0
  while l < r:
    
      if (people[l] + people[r])<= limit:
        l += 1 
        r -= 1 
      else:
        r -= 1 
      count += 1 
  if l == r: 
    count += 1 
  return count 
    
