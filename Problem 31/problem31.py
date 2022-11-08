# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character insertions, deletions, 
# and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: 
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

def solve(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    count = 0
    for x in range(min(len1, len2)):
        if(str1[x] != str2[x]):
            count+=1
    count+=abs(len1-len2)
    return count

def main():
    print(solve("kitten", "sitting"))
    pass
if __name__ == "__main__":
    main()