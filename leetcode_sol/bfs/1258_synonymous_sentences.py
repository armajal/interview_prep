'''
Start: 19:45

You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings.
 You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically.

--------------------------------------------
Input: list of string pairs synonyms[i] = [string1, string2] are similar, sentence text
Output: all synonym sentences sorted
Constraint: many sentence combinations, for index i, sentence[i] = string simularity[i], sentence[:i] + string_simularity[i] + sentence[i+1:]
Tool: BFS or Union Find

Questions:
    Example?
        Example 1
        Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
        Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
        
        Example 2:
        Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
        Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]


Intuition:
        BFS. 
        1. Build adj list for string simularity pairs 
        2. For each word in sentence
             if word in adj_list:
                new_sentence = BFS(word, sentence)
                res.append(new_sentence)

End: 19:52, 7 minutess
'''

def generateSentences(synonyms: list[list[str]], sentence: str) -> list[str]:
    
    # 1. Build adj list: 
    adj_list = {}

    for synonym in synonyms:
        syn_a, syn_b = synonym[0], synonym[1]

        adj_list.setdefault(syn_a, []).append(syn_b)
        adj_list.setdefault(syn_b, []).append(syn_a)

    # 2. Build BFS
    res = set()
    queue = [sentence]
    visited = {sentence}

    while queue:
        curr_sentence = queue.pop(0)
        res.add(curr_sentence)
        words = curr_sentence.split()
    
        for idx, word in enumerate(words):

            for synonym in adj_list.get(word, []):
                if synonym not in visited:
                    
                    # 3. String maniuplation 
                    temp_sentence = " ".join(words[:idx] + [synonym] + words[idx + 1:])
                    if temp_sentence not in visited:
                        visited.add(temp_sentence)
                        queue.append(temp_sentence)



    return sorted(res)



# Test 1: 
synonyms = [["happy","joy"],["cheerful","glad"]]
text = "I am happy today but was sad yesterday"

print(generateSentences(synonyms, text))
# Errors sat 20:20, infinit loop 
# Solved 20:23 w/ visited Set
# Output: {'I am happy today but was sad yesterday', 'I am joy today but was sad yesterday'}

# Test 2 
'''
 Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
        Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
        
'''
synonyms2 = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text2 = "I am happy today but was sad yesterday"
print(generateSentences(synonyms2, text2))
# Errors: Not lexigraphically sorted 20:26, Not all solutions 20:28
# Fixed and passes 20:41 (used Claude to fix BFS)

'''
Union Find would've provided O(1) look up and not had to do everything o granularly 

'''
