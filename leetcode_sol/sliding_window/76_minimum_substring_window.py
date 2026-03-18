'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
-------------------------
14:32pm 

Input: 2 strings w/ m & n lengths 
Output: str -> min substring of s where every character in t window
Constraint: even duplicatess
Tool: sliding window


Approach:

    1. collect count and char, for every char in t
    2. have = {}, need = {}, satisfied = 0, required = len(t), start = 0, end in loop '
        for char in s
            if char in need, add to have, increment have, required, and satisfied.
                if satisfied, decrement start

            else
                decrement start and move accordingly 
 
'''

def find_min_substring(s: str, t: str):
    have = {}
    need = {}
    satisfied = 0
    best_str = ""
    min_len = float('inf')
    start = 0 

    for letter in t:
        need[letter] = need.get(letter, 0) + 1
    
    required = len(need)

    for end in range(len(s)):
        curr_char = s[end]
        have[curr_char] = have.get(curr_char, 0) + 1 
        if curr_char in need:
            if have[curr_char] == need[curr_char]:
                satisfied += 1

                while satisfied == required:
                    if min_len > end - start + 1:
                        min_len = end - start + 1 
                        best_str = s[start:end+1]
                    
                    
                    start_char = s[start]
                    have[start_char] -= 1

                    if start_char in have and start_char in need and have[start_char] < need[start_char]:
                        satisfied -= 1

                    start += 1
    return best_str

'''
14:46 Testing
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''
# 14:49 Empty output
print(find_min_substring("ADOBECODEBANC", "ABC")) # Expected "BANC"


print(find_min_substring("a", "a"))


# Passed w/ referencing sliding window outline @ 15:04 

print(find_min_substring("aa", "aa")) # Failed on leetcode 