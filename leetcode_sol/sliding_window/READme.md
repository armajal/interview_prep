

## Sliding Windows

- Variable or fixed length

# Algorithm 
 1. 2 pointers *start* and *end* , 1 *max var* = 0 , 1 *state* data structure to store current window contents. Gather window size as k. 
 2. Increment *end*
    2b. Add arr[end] to *state* and increment it's count. 
    2c. if len(state) is <= k, test for window end-start > *max var*
3. Contract window
 3b. Decrement count of arr[start] in *state*
 3c. Increment *start* pointer until end-start+1 is within k
 - Notes: 
 - Window = end - start + 1 
 - dcitionary is very helpful but set is good for without repeat
 - the loop is usually 'for end in range(len(given_var))'
 
# Complexity
- O(n) where n is length of input array
- *end* pointer iterates through input array once. *start* pointer iterates through input array at most once
- O(1) time to check if its invalid
- O(1) Space Complexity because state is linear

# When to use
- Any search for contiguous subarray/substring in array/string with a constant contraints
- If(length of sub-item is known), use fixed. Else, variable. 
- Ex:
    1. Find largest substring without repeating chars (variable)
    2. Find largest substring containing a single character that can be replaced at most k chars (variable)
    3. Find largest sum of sub of size k without duplicate elements in given array (fixed)