# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

#Approach: I actually tackled this before on an interview!

# we can use a fourth of a circle rather than a full circle, so area of a circle would be Pir^2 = a/4

import math
from random import Random, random

randomPoints = []
def initializeArray(n):
    global randomPoints
    randomPoints = [[random() for x in range(2)] for y in range(n)]



def solve():
    global randomPoints
    insideCirc = 0
    for p in randomPoints:
        dist = math.sqrt((p[0]*p[0]) + (p[1]*p[1]))
        if(dist<1):
            insideCirc+=1
    
    return 4* insideCirc/len(randomPoints)
    pass

def main():
    initializeArray(10000)
    print(solve())
    pass

if __name__ == "__main__":
    main()