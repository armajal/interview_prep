'''
Creating a window that slides and instead of constantly adding up the same elements you add and subtract in the window. 
O(n) - Every element exits and enters just once from O(n * k)
'''

def fixed_sliding_window(arr: [int], window: int) -> int: 
    start = 0
    window_sum = 0
    max_sum = float('-inf')

    for end in range(len(arr)):
        window_sum += arr[end]

        if end - start + 1 == k:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[start]
            start += 1
    
    return max_sum

# Longest
def variable_sliding_window(arr: str) -> int:
    start = 0
    values_set = set()
    max_len = 0

    for end in range(len(arr)):
        while arr[end] in values_set:
            values_set.remove(arr[start])
            start += 1
        
        values_set.add(arr[end])
        max_len = max(max_len, end - start + 1 )
    return max_len

# Shortest
def shortest_sliding_window(arr:[], find:str ) -> int:
    start = 0
    values_dict = dict()
    min_len = float('inf')

    for letter  in find:
        values_dict.setdefault(letter, 0) += 1

    have = {}
    satisfied = 0
    required = len(values_dict)
    best_arr = []

    for end in range(len(arr)):
        char = arr[end]

        have[char] = have.get(char, 0) + 1

        if char in values_dict and have[char] == values_dict[char]:
            satisfied += 1

        while satisfied == required:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                best_arr = arr[start:end + 1]

            start_char = arr[start]
            have[start_char] -= 1
            if start_char in values_dict and have[start_char] < values_dict[start_char]:
                satisfied -= 1
            start += 1
    return best_arr



'''
Tests for longest substring
'''   
print(variable_sliding_window("abcabcbb"))

print(variable_sliding_window("netflix"))

print(variable_sliding_window("needajob"))

print(variable_sliding_window(""))
            


        