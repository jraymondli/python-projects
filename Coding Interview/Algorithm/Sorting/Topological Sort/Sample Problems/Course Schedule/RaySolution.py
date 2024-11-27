from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):

    p_dict = defaultdict(lambda:[])
    d_dict = defaultdict(lambda:[])
    
    for a, b in prerequisites:
      p_dict[a].append(b)
      d_dict[b].append(a)
      
    dq = deque()
    for i in range(num_courses):
      if len(p_dict[i]) == 0: dq.append(i)
      
    visited = set()
    while dq: 
      c = dq.popleft()
      visited.add(c) 
      for n_c in d_dict[c]:
        p_dict[n_c].remove(c)
        if len(p_dict[n_c]) == 0: 
          dq.append(n_c)
      
    return len(visited) == num_courses
