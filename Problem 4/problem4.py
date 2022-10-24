# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def solve(arr):
    arr.sort()
    intresult = arr[0]
    for x in range(len(arr)):
        if(arr[x]-intresult<=1 or arr[x] <=0):
            intresult= arr[x]
        else:
            while(intresult!=arr[x]):
                intresult+=1
                if(intresult>0 and intresult!=arr[x]):
                    return intresult


    return intresult+1


def main():
    arr1 = [3, 4, -1, 1]
    arr2 = [1, 2, 0]
    arr3 = [-3,-1, 1, 3] ##should return 2
    arr4 = [-3,-1, 2] ##should return 1
    print(solve(arr1))
    print(solve(arr2))
    print(solve(arr3))
    print(solve(arr4))


if __name__ == "__main__":
    main()