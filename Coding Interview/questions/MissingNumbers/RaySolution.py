def find_disappeared_numbers(nums):
    n = len(nums)
    
    # Cycle sort to place elements in their correct positions
    for i in range(n):
        while nums[i] != nums[nums[i] - 1]:
            # Swap nums[i] with the element at its target position nums[nums[i] - 1]
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
    # Identify missing numbers
    result = []
    for i in range(n):
        if nums[i] != i + 1:
            result.append(i + 1)
    
    return result
