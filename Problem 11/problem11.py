# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
ENDS_HERE = '__ENDS_HERE'

class Trie(object):
    def __init__(self):
        self._trie ={}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie: ##if char doesnt exist, create a char for the word
                trie[char] = {}
            trie = trie[char] ## Replace current trie's char with the next one.
        trie[ENDS_HERE] = True ##on the final letter's trie, add a value to check if the word is done
    
    def elements(self, prefix): ##Get elements using prefix
        d= self._trie
        for char in prefix:
            if char in d:
                d = d[char] ##Get the trie for each char
            else:
                return []
        return self._elements(d) ##Go to the enxt step after going to the latest possible trie given the suffix
    
    def _elements(self, d):
        result = []
        for c, v in d.items(): ##for key c with value v 
            if c == ENDS_HERE: ##if the key is ends here
                subresult = ['']  ##Finish substring
            else:
                subresult = [c+ s for s in self._elements(c)] ##otherwise, add the char+every other element on the next Trie
            result.extend(subresult) ##extend the list with the subresult
        return result #return the substrings


    
trie = Trie()

def solve(s):

    suffixes = trie.elements(s)
    return [s+w for w in suffixes] ##Return suffix+rest of the words in an array.

def main():
    s1= "de"
    s2 = "pe"
    query = ["penis", "pensive", "poggers", "dog", "deer", "deal"]
    
    for x in query:
        trie.insert(x)

    print(str(solve(s1)))
    print(str(solve(s2)))
    pass

if __name__ == "__main__":
    main()

# def solve(s, query):
#     result = []
#     query.sort()

#     for x in query:
#         if x[0:len(s)] == s:
#             result.append(x)

#     return result