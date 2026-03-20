'''

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.



Input: string with whitesspace and signed
Output: int
Constraint: skip white space, round, convert and round


Approach
    signedness, stack
    for each char in s:
        if whitespace ignore
        if -, signedness = false, else true
        push each number unto stack
    
    base10 = 0
    val = 0
    while stack
        val += int(stack.pop) * pow(10, base10)
    return val
'''

def string_to_inti(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
    
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1
    
    val = 0
    while i < len(s) and s[i].isdigit():
        val = (val * 10) + s[i]
        i+= 1

    val *= sign
    val = max(-2**31, min(val, 2**31 - 1))
