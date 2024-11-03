To solve this problem using **Cycle Sort** with \( O(n) \) time complexity and \( O(1) \) space complexity, we can rearrange elements in place so each element is in its correct position (i.e., `nums[i] = i + 1` for an array indexed from `0`). Once we do this, we can iterate through the array to identify any missing numbers.

Here’s the step-by-step approach:

### Approach

1. **Cycle Sort**: 
   - Iterate through the array and place each element `nums[i]` at its correct index (i.e., `nums[i]` should ideally be placed at `nums[nums[i] - 1]`).
   - If `nums[i]` is not at the correct index and `nums[i]` is within the range `[1, n]`, swap `nums[i]` with the element at `nums[nums[i] - 1]`.
   - Repeat until each element is either at the correct position or out of bounds.

2. **Identify Missing Numbers**: 
   - After arranging the array, any number that is not at the correct index indicates a missing number.
   - Iterate through the array, and if `nums[i] != i + 1`, then `i + 1` is missing from the array.

### Code Implementation

Here’s the Python code implementing the above approach:

```python
def findDisappearedNumbers(nums):
    n = len(nums)
    
    # Cycle sort to place elements in their correct positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            # Swap nums[i] with the element at its target position nums[nums[i] - 1]
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
    # Identify missing numbers
    result = []
    for i in range(n):
        if nums[i] != i + 1:
            result.append(i + 1)
    
    return result
```

### Explanation of the Code

1. **Cycle Sort Loop**:
   - For each element `nums[i]`, we place it in its correct position by swapping it with `nums[nums[i] - 1]` until each element is either out of the range or in the correct position.

2. **Collecting Missing Numbers**:
   - After rearranging, if an element at index `i` is not equal to `i + 1`, then `i + 1` is missing from the array.
   - Collect all such missing numbers in the `result` list.

### Complexity Analysis

- **Time Complexity**: \( O(n) \), because each element is placed at its correct position in at most one swap.
- **Space Complexity**: \( O(1) \), as we are modifying the input array in place and only using a constant amount of additional space for the result.

### Example

```python
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))  # Output: [5, 6]
```

In this example:
- After rearranging, the array becomes `[1, 2, 3, 4, 3, 2, 7, 8]`.
- Positions 4 and 5 don’t match with `5` and `6`, so `5` and `6` are missing numbers.
