# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.
def solve(string):
    def CheckOpen(let):
        if(let == '[' or let == '(' or let == '{'):
            return True
        else:
            return False
        
    def Matches(let1, let2):
        if(let1 == "[" and let2 == "]"):
            return True
        if(let1 == "(" and let2 == ")"):
            return True
        if(let1 == "{" and let2 == "}"):
            return True
        else:
            return False

    stack = ""
    for letter in string:
        if(not CheckOpen(letter)):
            if(len(stack)== 0):
                return False
            if(Matches(stack[-1], letter)):
                stack = stack[:-1]
            else:
                return False

        elif(CheckOpen(letter)):
            stack+=letter
        
    if(stack == ""):
        return True
    else:
        return False
        
def main():
    print(solve("([])[]({})"))
    print(solve("((()"))
    print(solve("([)]"))
    pass

if __name__ == "__main__":
    main()