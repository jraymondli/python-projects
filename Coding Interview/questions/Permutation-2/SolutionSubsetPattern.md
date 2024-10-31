Certainly! A subset pattern approach for generating unique permutations involves treating each number as a choice: either including it in the current permutation or not. However, unlike typical subset generation, here we need to build complete permutations while ensuring all permutations are unique.

One effective way to apply this pattern is by recursively choosing each element in the list and keeping track of used elements to avoid duplicates. Here’s how we can implement this:

```python
def unique_permutations(nums):
    def backtrack(path, counter):
        # If the path length equals nums length, we've formed a valid permutation
        if len(path) == len(nums):
            result.append(path[:])
            return
        # Iterate over elements, allowing each unique number to be used
        for num in counter:
            if counter[num] > 0:  # Only use numbers with a positive count
                # Choose the number and add to the path
                path.append(num)
                counter[num] -= 1
                backtrack(path, counter)
                # Backtrack: remove the number from the path and restore its count
                path.pop()
                counter[num] += 1

    # Count occurrences of each number to handle duplicates
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    result = []
    backtrack([], counter)
    return result
```

### Explanation

1. **Counter Dictionary**: We create a dictionary `counter` to keep track of the frequency of each element in `nums`. This allows us to skip duplicates by only adding each unique number when it’s available in `counter`.
2. **Backtracking with Subset Pattern**: For each recursive call:
   - If the `path` length matches `nums`, we add it to `result`.
   - For each unique number in `counter`, we attempt to add it to `path` if it hasn’t been fully used up. We decrement its count in `counter`, recurse, and then backtrack by restoring the count.
3. **Recursive Depth and Subsets**: The recursion explores each subset of `nums` by attempting each unique element, similar to a subset approach.

### Complexity

- **Time Complexity**: \( O(n \cdot n!) \), as we need to generate all unique permutations.
- **Space Complexity**: \( O(n) \), for the recursion depth and `counter` dictionary storage.

### Example Usage

```python
nums = [1, 1, 2]
print(unique_permutations(nums))
```

Output:

```python
[[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

This subset-pattern solution leverages the concept of choosing each element only once per position, avoiding duplicates by using the frequency count of each element.
