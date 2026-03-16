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

def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
    
    # 1. Build adj list: 
    adj_list = {}

    for synonym in synonyms:
        syn_a, syn_b = synonym[0], synonym[1]

        adj_list.setdefault(syna, []).append(syn_b)
        adj_list.setdefault(synb, []).append(syn_a)

    # 2. Build BFS
    res = [] 
    for word in sentence.split(" "):
        if word in adj_list: # We've reached a synonym, Start bfs
            
            queue = [word]
            visited = set()
            visited.add(word)

            while queue:
                curr_word = queue.pop(0)
                for synonym in adj_list[curr_word]:
                    queue.offer(synonym)
                    idx = sentence.split(" ").get(synonym)
                    temp_sentence = sentence[:idx] + synonym + sentence[idx + 1:]
                    res.append(temp_sentence)
    return res



# 20:03, 18 minutes
# Test 1: 
synonyms = [["happy","joy"],["cheerful","glad"]]
text = "I am happy today but was sad yesterday"

print(generateSentences(synonyms, text))
