# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, 
# return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


class Trie(object):
    def addWord(self, word):
        currentLetter = self.letterbase
        for letter in word:
            if(letter not in currentLetter):
                currentLetter[letter] = {}
            currentLetter = currentLetter[letter]
        currentLetter["Finished"] = True ##Word is finished
        pass

    def __init__(self, set):
        self.letterbase = {}
        self.setbase = set
        for word in set:
            self.addWord(word)
        #print(str(self.letterbase))
    
    def findWordSet(self, word):
        currentWord = ""
        currentTrie = self.letterbase
        wordsToReturn = []
        for letter in range(len(word)):
            currentWord+=word[letter]
            currentTrie = currentTrie[word[letter]]
            if ("Finished" in currentTrie):
                currentTrie = self.letterbase
                wordsToReturn.append(currentWord)
                currentWord = ""
        print(str(wordsToReturn))
        return wordsToReturn


    

def solve(set, word):
    trie = Trie(set)
    trie.findWordSet(word)
    pass

def main():
    solve(["bed", "bath", "bedbath", "and", "beyond"], "bedbathandbeyond")
    solve(['quick', 'the', 'fox',  'brown'], "thequickbrownfox")
    pass

if __name__ == "__main__":
    main()