#!/usr/bin/env python3

def integer_mirror(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
        
    if n == 0:
        return 0

    reversed_n = 0
    temp_n = n

    while temp_n > 0:
        digit = temp_n % 10
        reversed_n = (reversed_n * 10) + digit
        temp_n = temp_n // 10

    return reversed_n

if __name__ == "__main__":
    test_inputs = [315, 400, 7, 0, 12345]
    print(f"{'Input':<10} | {'Output':<10}")
    print("-" * 25)
    for num in test_inputs:
        result = integer_mirror(num)
        print(f"{num:<10} | {result:<10}")

