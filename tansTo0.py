class Solution:

    def minimumOneBitOperations(self, n: int) -> int:

        def bitString(n):
            bs = ''
            while n:
                bs = str(n % 2) + bs
                n = n // 2
            return bs

        def setBit(k, bs):
            print(k, bs)
            pos = bs.find('1')
            if pos == -1: bs = ''
            if bs == '': return pow(2, k + 1) - 1

            bs = bs[pos:]
            lbs = len(bs)
            assert (k >= lbs)

            count = 0
            if lbs == k:
                count = clearBits(bs[1:])
                count += 1
                count += clearBit(k - 1)
            else:
                count = setBit(k - 1, bs)
                count += 1
                count += clearBit(k - 1)

            return count

        def clearBit(k):
            return pow(2, k + 1) - 1

        def clearBits(bs):
            pos = bs.find('1')
            if pos == -1: return 0

            bs = bs[pos:]

            lbs = len(bs)
            if lbs == 0: return 0
            if lbs == 1: return 1

            if bs[1] == '1':
                count = clearBits(bs[2:])
                count += 1
                count += clearBit(lbs - 1 - 1)
            else:
                count = setBit(lbs - 1 - 1, bs[2:])
                print("cp1:", lbs, bs[2:], count)
                count += 1
                count += clearBit(lbs - 1 -1)

            return count

        bits = bitString(n)
        return clearBits(bits)

# tests
#   n = 0

# performance
#  optimization with @lru_cache
#
s = Solution()
print(s.minimumOneBitOperations(9))


