class Solution:
def variable_length_sliding_window(nums):
  state = # choose appropriate data structure
  start = 0
  max_ = 0

  for end in range(len(nums)):
    # extend window
    # add nums[end] to state in O(1) in time

    while state is not valid:
      # repeatedly contract window until it is valid again
      # remove nums[start] from state in O(1) in time
      start += 1

    # INVARIANT: state of current window is valid here.
    max_ = max(max_, end - start + 1)

  return max_

    def characterReplacement(self, s: str, k: int):
        max_val = 0
        start = 0 
        max_valid_window = 0
        seen = {}

        for end in range(len(s)):
            char = s[end]

            seen[char] = seen.get(char, 0) + 1 
            max_val = max(max_val, seen[char])

            while (end - start + 1) - max_valid_window > k:
                left_char = s[start]
                char_count[left_char] -= 1
                start += 1

            max_valid_window = max(max_valid_window, end - start + 1)


