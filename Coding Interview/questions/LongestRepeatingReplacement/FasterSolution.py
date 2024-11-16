def find_longest_substring(input_str):
    if len(input_str) == 0:
        return 0

    window_start, longest, window_length = 0, 0, 0

    last_seen_at = {}

    for index, val in enumerate(input_str):
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            if last_seen_at[val] >= window_start:
                window_length = index - window_start
                if longest < window_length:
                    longest = window_length
                window_start = last_seen_at[val] + 1

            last_seen_at[val] = index

    index += 1

    if longest < index - window_start:
        longest = index - window_start

    return longest
