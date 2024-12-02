from heapq import heappush, heappop

def min_refuel_stops(target, start_fuel, stations): 

  if start_fuel >= target: return 0 
  
  hq = [] 
  fuel = start_fuel 
  count = 0 
  for d, f in stations:

    if fuel >= d: 
      heappush(hq, -f)
      continue 
    
    while fuel < d and len(hq) > 0:
      fuel += - heappop(hq)
      count += 1
    
    print(d, f, fuel, hq)
    if fuel >= target: return count 
    
    if fuel < d: 
      return -1 
    heappush(hq, -f)
  
  while fuel < target and len(hq) > 0:
    fuel += - heappop(hq)
    count += 1
    
  if fuel >= target: return count 
  return -1 
