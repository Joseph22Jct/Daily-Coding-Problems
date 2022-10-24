# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
# write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, 
# if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

## Approach: there's clearly a formula for this:
##

def recursive(n, set, resultSoFar, allResults):
    ##print("Current N ="+ str(n)+ " with resultSoFar = " + str(resultSoFar)+ " and all Results: " + str(allResults))
    for x in set:
        if(x<=n):
            result = resultSoFar.copy()
            result.append(x)
            newN = n-x
            recursive(newN, set, result, allResults)
        elif(n == 0):
            #print("New Entry! "+ str(resultSoFar))
            allResults.append(resultSoFar)
            return allResults
    return allResults

def solve(n, set =[]):
    if(set == []):
        set = [1,2]
    set.sort() ##sort 
    waysToClimb = []
    waysToClimb = recursive(n, set, [],[])
    print(str(waysToClimb))
    print(str(len(waysToClimb))+ " ways to climb the stairs with set: "+ str(set))

    pass

def main():
    solve(3)
    solve(4)
    solve(5)
    solve(5, [1,3,5])
    pass

if __name__ == "__main__":
    main()