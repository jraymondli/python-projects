def integer_addition(a: int, b: int) -> int:
    # 32-bit mask in hexadecimal
    mask = 0xFFFFFFFF
    # Loop until there is no carry
    while b != 0:
        # Calculate sum without carry
        temp = (a ^ b) & mask
        # Calculate carry
        b = ((a & b) << 1) & mask
        a = temp
    # If a is negative, convert it to a negative 32-bit integer
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)
