# with dynamic programming

def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    # Table to keep track of palindromic substrings
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    # Check for two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_len = i, 2

    # Check for palindromes longer than two characters
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Check if the current substring is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_len = i, length

    return s[start:start + max_len]
