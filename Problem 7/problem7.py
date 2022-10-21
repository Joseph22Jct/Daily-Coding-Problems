# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.
result = []

def recursion(input, currentString):
    global result
    if(len(input)>1):
        if(int(input[0]+input[1]) <=25 and int(input[0]) != 0):
            newString= currentString+ chr(int(input[0]+input[1])+96) ## 'a' is ASCII 97
            newInput = input[2:]
            recursion(newInput, newString)
    if(len(input)>0 and int(input[0]) != 0):
            newString= currentString+ chr(int(input[0])+96) ## 'a' is ASCII 97
            newInput = input[1:]
            recursion(newInput, newString)
    if(len(input)==0):
        result.append(currentString)
        print(str(result))
        return 
        

    

def solve(input):
    global result
    input = str(input)
    result = []
    recursion(input, "")
    print(str(result))
    print(len(result))



def main():
    input1 = 111
    input2 = 210
    input3 = 85232

    solve(input1)
    solve(input2)
    solve(input3)
    pass


if __name__ == "__main__":
    main()