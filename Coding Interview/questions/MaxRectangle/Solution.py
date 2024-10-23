# this solution passes all test cases

def largest_rectangle(heights):

    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        # If this bar is higher than the bar at stack top, push it to the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top
            top_of_stack = stack.pop()
            # Calculate the area with heights[top_of_stack] as the smallest (or minimum height) bar
            area = heights[top_of_stack] * (index if not stack else index - stack[-1] - 1)
            # Update max area, if needed
            max_area = max(max_area, area)

    # Now pop the remaining bars from the stack and calculate area
    while stack:
        top_of_stack = stack.pop()
        area = heights[top_of_stack] * (index if not stack else index - stack[-1] - 1)
        max_area = max(max_area, area)

    return max_area



    
  
