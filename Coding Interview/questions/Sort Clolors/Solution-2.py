def sort_colors(colors):
    start, current, end = 0, 0, len(colors) - 1
    
    while current <= end:
        if colors[current] == 0:
            colors[start], colors[current] = colors[current], colors[start]
            current += 1
            start += 1

        elif colors[current] == 1:
            current += 1

        else:
            colors[current], colors[end] = colors[end], colors[current]
            end -= 1
    return colors
