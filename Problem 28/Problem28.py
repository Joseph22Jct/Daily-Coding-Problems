# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary 
# so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


def solve(list, k):
    solution = []
    current = []
    for x in range(len(list)):
        stri = ""
        for w in current:
            stri+=w
        
        if(len(stri+list[x])<= k - len(current) and x < len(list)-1):
            current.append(list[x])
        else:
            stringToAdd = ""
            stringToAdd+=current[0]
            if(len(current)==1):
                for add in range(k-len(current[0])):
                    stringToAdd+=" "
            else:
                spacesToAdd = []
                amountOfLetters = 0
                for y in range(len(current)):
                    amountOfLetters+= len(current[y])
                spc = k-amountOfLetters
                evenSpaces = int(spc/(len(current)-1))
                remnants = spc%(len(current)-1)
                for y in range(len(current)-1):
                    spacesToAdd.append(evenSpaces)

                for y in range(remnants):
                    spacesToAdd[y] +=1

                finalString = ""
                for y in range(len(current)):
                    finalString+=current[y]
                    if (y< len(spacesToAdd)):
                        for s in range(spacesToAdd[y]):
                            finalString+=" "
            solution.append(finalString)
            current = []
            current.append(list[x])
    return solution

def main():
    list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    print(str(solve(list, 16)))
    

if __name__ == "__main__":
    main()