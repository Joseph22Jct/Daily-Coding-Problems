# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

def recurssion(array,k, arrayToReturn = []):
    if k<=len(array):
        arrayToReturn.append(max(array[0:k]))
        recurssion(array[1:], k, arrayToReturn)
    return arrayToReturn

def solve(array,k):
    sol = recurssion(array, k)
    print(str(sol))
    pass

def main():
    solve( [10, 5, 2, 7, 8, 7], 3)
    pass

if __name__ == "__main__":
    main()