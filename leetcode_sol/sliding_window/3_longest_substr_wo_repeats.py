'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

#15:24 pm 
Input: s
Output : int -> max len of substring W/O Dupes
Constraint: NO DUPLICATE Chars
Tool:Sliding window

Approach:
    1. max_len = 0, chars_dict = {}, start = 0
    2. for curr end in s:
        add s[end] to chars_dict
        while curr in chars_dict > 1:
            max_len = max(end-start + 1, max_len)
            constraint window: remove s[start], increment start 


'''
#15:27
from collections import defaultdict

def longest_substr_wo_repeats(s: str) -> int:
    if len(s) == 1:
        return 1
    
    chars_dict = defaultdict(int)
    max_len = 0 
    start = 0

    for end in range(len(s)):
        curr = s[end]
        chars_dict[curr] = chars_dict[curr] + 1

        while chars_dict[curr] > 1:
            start_char = s[start]
            chars_dict[start_char] -= 1
            start += 1
        max_len = max(end-start + 1, max_len)

    return max_len

# 14:32 Tests
print(longest_substr_wo_repeats("abcabcbb")) # 14:33 Failed w/ 0 len | Passed 15:35pm 

print(longest_substr_wo_repeats("bbbbb"))

print(longest_substr_wo_repeats("pwwkew"))

#All tests passed 15:36

#LC Failed  | Passed at 15:37 w/ edge case handling
print(longest_substr_wo_repeats(" "))

# All testss passed @ 15:40 on LC. Fixed bug w/ test case below. Max_len was calcualted when constraining window which doesn't exist for this test
print(longest_substr_wo_repeats("au"))
