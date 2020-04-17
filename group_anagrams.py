import collections

"""Given an array of strings, group anagrams together.

    Example: 
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output:
    [
     ["ate", "eat", "tea"],
     ["nat", "tan"],
     ["bat"]
    ]

- All inputs will be in lowercase.
- The order of your output does not matter.
"""

""" Thought process:
- split up each word
- create defaultdict(list)
    - key is tuple of sorted word with value as list of the words
    - keep appending to list if the sorted word is the same as the key
- return the values of the dict
"""

def group_anagrams(words):
    
    anagrams = collections.defaultdict(list)
    for word in words:
        word_letters = tuple(sorted(word))
        anagrams[word_letters].append(word)
    return anagrams.values()


        

