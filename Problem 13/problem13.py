# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

##Approach: This sounds like a problem you could use Trie's again. if you use a trie, maybe a tuple!
##This should be read left to right, perhaps for every letter, store said letter, and make k-1
##then make recursive for k, and reduce k by -1 if k is different as well as start a new k on that slot, and if k is = 0, add that string to the results.
##Then check if those results by length and return the longest.


def recursive(ogk, k, s,currentsS, results):
    def AddEntry():
        results.append(currentsS)
        return results
        
    #print("s is: " + s+ ", and currentsS is: "+ currentsS)

    if (k==0 and len(s)==0):
        AddEntry()

    elif(k == 0):
        if(s[0] in currentsS):
            currentsS+=s[0]
            s = s[1:]
            recursive(ogk, k, s, currentsS, results)
            recursive(ogk,ogk,s, "", results)
        else:
            AddEntry()

    elif (k>0 and len(s)!=0):
        if(s[0] not in currentsS):
            k-=1
        currentsS+=s[0]
        s = s[1:]
        recursive(ogk, k, s, currentsS, results)
        recursive(ogk,ogk,s, "", results)
        
    return results

def solve(k, s):

    results = recursive(k, k, s, "", [])
    results = sorted(results, key=len)
    print(str(results))
    return results[-1]

def main():
    print(solve(2, "abcba"))
    print(solve(3, "abcbaab"))
    pass

if __name__ == "__main__":
    main()