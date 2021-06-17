from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        UPPER_LS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        fl = len(formula)
        stack = []
        curr_array = []

        for i in range(fl):

            if formula[i] >= 'A' and formula[i] <= 'Z':
                ele = formula[i]
                count = 0
            elif formula[i] >= 'a' and formula[i] <= 'z':
                ele += formula[i]
            elif formula[i].isdigit():
                count *= 10
                count += int(formula[i])
            elif formula[i] == '(':
                stack.append(curr_array)
                curr_array = []
                print("point1, curr_array:", curr_array)
                print("point1, top of stack:", stack[-1])
                continue
            elif formula[i] == ')':
                ele = curr_array
                count = 0
                curr_array = stack.pop()

            if (i == (fl - 1)) or (formula[i + 1] in (UPPER_LS + '()')):
                if count == 0: count = 1
                curr_array.append([ele, count])
                if stack:
                    print("point 2:", curr_array)
                    print("point2:", stack[-1])

        def expandArray(array):
            ra = []
            for elem, count in array:
                if isinstance(elem, list):
                    suba = expandArray(elem)
                    subb = [[e, c * count] for e, c in suba]
                    ra.extend(subb)
                else:
                    ra.append([elem, count])
            return ra

        #print(curr_array)
        #return curr_array

        expanded_array = expandArray(curr_array)
        elemDict = defaultdict(lambda: 0)
        for elem, count in expanded_array:
            elemDict[elem] += count
        ta = [[e, c] for e, c in elemDict.items()]
        ta.sort()
        output = ''
        for e, c in ta:
            output += e
            if c > 1:
                output += str(c)
        return output


s = Solution()
print(s.countOfAtoms('Mg(OH)2'))