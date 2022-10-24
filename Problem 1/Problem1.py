
# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def solve(arr, k):
    arr.sort(reverse = True)
    for x in arr:
        if(k > x):
            numbertoLook = k-x
            for y in arr:
                if(y == numbertoLook and x!=y): ##Program assumes you cant choose the same number twice
                    
                    print("Found one with "+ str(x) + " and "+str(y) +", where k is "+ str(k) + " and array of " + str(arr))
                    return True
    print(False)
    return False
    

if __name__ == "__main__":
    arr1 = [10, 15, 3, 7]
    arr2 = [5, 2, 3, 10]
    arr3 = [2, 15, 7, 8]
    k1 = 4
    k2 = 9
    k3 = 13
    solve(arr1, k1) ##Should be false
    solve(arr1, k2) ##Should be false
    solve(arr1, k3) ##Should be true (10+3)
    solve(arr2, k1) ##Should be false
    solve(arr2, k2) ##Should be false
    solve(arr2, k3) ## Should be true
    solve(arr3, k1) ##Should be false
    solve(arr3, k2) ##Should be true (2+7)
    solve(arr3, k3) ##Should be false



