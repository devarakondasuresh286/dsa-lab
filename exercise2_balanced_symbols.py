#!/usr/bin/env python3
 
def symbol_checker(symbol_string):
 
    stack = []
    opening = "([{"
    closing = ")]}"
    matches = {")": "(", "]": "[", "}": "{"}
 
    for char in symbol_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != matches[char]:
                return False
 
    return len(stack) == 0
 
if __name__ == "__main__":
    test_inputs = [
        "{{([][])}}",
        "[[{{}}]]",
        "[({})]",
        "{())",
        "[(])",
        "((()"
    ]
    
    print(f"{'Input':<20} | {'Output':<10}")
    print("-" * 35)
    for s in test_inputs:
        result = symbol_checker(s)
        print(f"{s:<20} | {result}")
 
 
