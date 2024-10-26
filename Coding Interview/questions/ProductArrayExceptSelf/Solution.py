    def product_except_self(nums):
        
        n = len(nums)
        left = [1] *n 
        for i in range(1, n):
          left[i] = nums[i-1] * left[i-1]
        right = [1] * n 
        for i in range(n-2, -1, -1):
          right[i] = right[i+1] * nums[i+1]
        res = []
        for i in range(n):
          res.append(left[i] * right[i])
        return res
