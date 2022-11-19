# Good morning! Here's your coding interview problem for today.

# This problem was asked by Quora.

# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
# If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). 
# There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

##Maybe select a pivot letter and add to list, then return 
def CheckForPalindrome(strng):
    # 5 letters means 2.5... which is 0-4, 1-3 and thats it
    letToCheck = int(len(strng)/2)
    for x in range(letToCheck):
        if(strng[x] != strng[-x-1]):
            return False
    return True

def solve(strng):
    if(CheckForPalindrome(strng)):
        return True
    

    pass


def main():
    solve("race")
    solve("google")
    pass

if __name__ == "__main__":
    main()