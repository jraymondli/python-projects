class Solution:
    def findLength(self, nums1, nums2) -> int:

        n1 = len(nums1)
        n2 = len(nums2)
        print("n1, n2:", n1, n2)
        maxSub = 0
        s1 = 0

        while s1 < n1:

            for s2 in range(n2):

                e1 = s1
                e2 = s2

                count = 0
                while nums1[e1] == nums2[e2]:
                    count += 1
                    e1 += 1
                    e2 += 1
                    if e1 == n1 or e2 == n2:
                        break
                if count > maxSub: maxSub = count

                if maxSub == n1 or maxSub == n2:
                    print("got here")
                    return maxSub

            s1 = (e1 + 1) if (s1 == e1) else e1

        return maxSub


s = Solution()
a = []
b = []
for i in range(1000):
    a.append(0)
    b.append(0)

print("maxSub length:", s.findLength(a, b))