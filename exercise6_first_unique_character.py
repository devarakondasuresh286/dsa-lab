#!/usr/bin/env python3
 
def first_unique_char_two_pass(s):
    if not s:
        return -1
    
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for index, char in enumerate(s):
        if freq[char] == 1:
            return index
    
    return -1
 
 
if __name__ == "__main__":
    test_cases = [
        "leetcode",
        "loveleetcode",
        "aabb",
        "dddccdbba",
        "",
        "a"
    ]
    
    print("Two-Pass Dictionary Approach")
    print(f"{'Input':<15} | {'Output':<5}")
    print("-" * 30)
    for s in test_cases:
        print(f"{s:<15} | {first_unique_char_two_pass(s)}")
 
 

 
