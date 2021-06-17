

def pBreadth(s):
    n = len(s)

    prev = None
    depth = 0
    maxBreadth = 0
    count = 0

    stack = []
    for i in range(n):

        if s[i] == '(':
            depth += 1
            if prev == '(':
                stack.append(count)
                count = 0
            prev = s[i]
        elif s[i] == ')':
            depth -= 1
            if prev == ')':
                if count > maxBreadth:
                    maxBreadth = count
                count = stack.pop()
                count += 1
            else:
                count += 1
            prev = s[i]

    maxBreadth = max(count, maxBreadth)
    return maxBreadth

print("breadth for empty string:", pBreadth(""))
print("breadth for ()()(()()()()()()())", pBreadth("()()(()()()()()()())"))
print("breadth for ()()(  ()()()()()    )", pBreadth("()()(  ()()()()()    )"))
print("breadth for ()()(  ()()()()()    )", pBreadth("()()(  ()()()()(  ()()()()()()  )    )"))