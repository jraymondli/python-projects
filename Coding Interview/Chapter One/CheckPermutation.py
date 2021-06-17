# Questions to ask:
# - white space
# - case
# - unicode or ASCII

from collections import defaultdict

def checkPermutatiions(s1, s2):

    n = len(s1)
    if n != len(s2):
        return False

    d1 = defaultdict(lambda : 0)
    d2 = defaultdict(lambda : 0)

    for i in range(n):
        d1[s1[i]] += 1
        d2[s2[i]] += 1

    for k, c in d1.items():
        if c != d2[k]: return False

    return True

print(checkPermutatiions("", "A"))
print(checkPermutatiions("ABC", "ACB"))
print(checkPermutatiions("ABAC", "CAAB"))

# Time Complexity O(N)
# Space Complexity O(N)