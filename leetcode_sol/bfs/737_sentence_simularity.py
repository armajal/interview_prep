'''

Start 9:38
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs 
where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is transitive. 
For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.

---------------------------------------------------------------
Input: two strings: sentence1, sentence2, array of string pairs 
Output: True if two Sentences are similar
Constraint: same length, and transitive words 
Intuition: BFS / Union Find 

9:42
    Union Find Approach:
       1. If 2 len sentences equal
       2. Union string similarity pairs, 
       3. For idx, words in sentence
            if word1 has relationship to word2 idx is assumed equal sentence[idx]:
                continue
            else:
                return False
        
        4. Return True

Edge Cases:
    - sentences w/ different lengths | False

Test Cases:

Example 1:

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Example 2:

Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: true
'''

#9:48
def sentence_similarity(simularity_pairs: list[list[str]], sentence1:str, sentence2: str) -> bool: 
    # Union Find Approach:
    # 1. If 2 len sentences equal
    if sentence1 is None or sentence2 is None or len(sentence1) != len(sentence2):
        return False

    # 2. Union string similarity pairs, 
    simularity_dict = defaultdict()
    def union(child_str: str, parent_str: str):
        simularity_dict[find(parent_str)] = find(child_str):

    def find(find_str: str):
        if simularity_dict[find_str] != find_str:
            simularity_dict[find_str] = find(find_str)
        return simularity_dict[find_str]
    
    for pairs in simularity_pairs:
        str1 = pairs[0]
        str2 = pairs[1]
        if str1 or str2 not in simularity_dict:
            simularity_dict[str1] = str1
            simularity_dict[str2] = str2
        union(str1, str2)
    
    '''
    # 3. For idx, words in sentence
            if word1 has relationship to word2 idx is assumed equal sentence[idx]:
                continue
            else:
                return False
    '''
    for idx, word in enumerate(sentence1):
        word2 = sentence2[idx]
        if find(word) != find(word2):
            return False
        else:
            continue

    #  4. Return True
    return True

#10:03 Tests
# Test 1:
sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]

print(sentence_similarity(similarPairs, sentence1, sentence2))
    
