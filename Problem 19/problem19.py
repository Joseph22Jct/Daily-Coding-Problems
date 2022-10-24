# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to 
# build the nth house with kth color, return the minimum cost which achieves this goal.

from cmath import inf


def solve(matrix):
    # newMatrix = []
    # for n in matrix:
    #     newMatrix.append(enumerate(n))
    
    housesValues = []
    for n in matrix:
        housesValues.append(n.index(min(n)))
    
    for n in range(len(housesValues)):
        if(n>=1 and n<len(housesValues)):
            if(housesValues[n]== housesValues[n-1]):
                tempCol = matrix[n]
                tempColM = matrix[n-1]
                tempVal = tempCol[housesValues[n]]
                tempValM = tempColM[housesValues[n-1]]
                tempColM[housesValues[n-1]] = inf
                tempCol[housesValues[n]] = inf
                if(tempVal - min(tempCol) > tempValM - min(tempColM)):
                    housesValues[n] = tempCol.index(min(tempCol))
                else:
                    housesValues[n-1] = tempColM.index(min(tempColM))
                


    print(str(housesValues))
    return housesValues
    pass

def main():
    solve([[100,80,80], [100,80,100], [100,80,80], [100,100,80]]) ##Using example
    solve([[100,80,50], [500,80,50], [30,80,70], [10,30,80]])
    pass

if __name__ == "__main__":
    main()
    pass