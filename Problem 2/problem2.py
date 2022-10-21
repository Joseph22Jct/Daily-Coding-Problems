# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def solve(input):
    copyarray = input.copy()
    returnArray = []
    for x in range(len(input)):
        print(str(x)+ " when " + str(len(copyarray)))
        copyarray.pop(x)
        productnumber = 1
        for y in copyarray:
            productnumber*=y
        returnArray.append(productnumber)
        copyarray= input.copy()
        
    print("The result of input "+str(input)+" is "+ str(returnArray))
    pass

def main():
    input1 = [1,2,3,4,5]
    input2 = [3,2,1]
    input3 = [1,3,5,7]
    solve(input1)
    solve(input2)
    solve(input3)
    pass

if __name__ == "__main__":
    main()