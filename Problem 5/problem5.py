# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

##this abomination of a function kicked my ass https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python

def cdr(f):
    def right(a,b):
        return b
    return f(right)
    # return f.__closure__[1].cell_contents alt solution

def car(f):
    def left(a,b):
        return a
    return f(left)
    # return f.__closure__[0].cell_contents

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def addition(a,b): ##Not part of the problem but this is blowing my mind
    return a+b

def main():
    test1 = cons(3,4)
    test1(print) ##You can do this??
    print(test1(addition))
    print(car(test1))
    print(cdr(test1))
    pass


if __name__ == "__main__":
    main()