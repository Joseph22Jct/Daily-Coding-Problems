# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start.
#  If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

#[[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, 
# since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

##Oh god this uses A* algorithm doesn it

import operator
from turtle import left


def calcDist(start,end):
    return abs(end[0]-start[0]) +abs(end[1]-start[1])

class Node(object):
    def __init__(self, start, end, location, parent=None):
        self.gcost = calcDist(location, end)
        self.hcost = calcDist(start, location)
        self.current = self.gcost+self.hcost
        self.location = location
        self.parent = parent
        pass



def solve(board, start, end):
    StartNode = Node(start, end, start)
    currentNode = StartNode
    possiblePaths = []
    pathsTotake = []
    traveledPaths = [].append(currentNode.location)
    
    while(currentNode.location!=end):
        upNode = [currentNode.location[0], currentNode.location[1]-1]
        if(currentNode.location[1]-1 >=0):
            if(board[currentNode.location[0]][currentNode.location[1]-1] != True):
                if (upNode not in pathsTotake and upNode not in traveledPaths):
                    possiblePaths.append(Node(start, end, (upNode[0],upNode[1]), currentNode))
                    pathsTotake.append(upNode)

        leftNode = [currentNode.location[0]-1, currentNode.location[0]]
        print(leftNode)
        if(currentNode.location[0]-1 >=0):
            if(board[currentNode.location[0-1]][currentNode.location[1]] != True):
                if (leftNode not in pathsTotake and leftNode not in traveledPaths):
                    possiblePaths.append(Node(start, end, (leftNode[0],leftNode[1]), currentNode))
                    pathsTotake.append(leftNode)

        rightNode = [currentNode.location[0]+1, currentNode.location[1]]
        if(currentNode.location[0]+1 < len(board[0])):
            if(board[currentNode.location[0]+1][currentNode.location[1]] != True):
                if (rightNode not in pathsTotake and rightNode not in traveledPaths):
                    possiblePaths.append(Node(start, end, (rightNode[0],rightNode[1]), currentNode))
                    pathsTotake.append(rightNode)

        downNode = [currentNode.location[0], currentNode.location[1]+1]
        if(currentNode.location[1]+1 <len(board)):
            if(board[currentNode.location[0]][currentNode.location[1]+1] != True):
                if (downNode not in pathsTotake and downNode not in traveledPaths):
                    possiblePaths.append(Node(start, end, (downNode[0],downNode[1]), currentNode))
                    pathsTotake.append(downNode)

        possiblePaths = sorted(possiblePaths, key=operator.attrgetter("current"), reverse=True)

        currentNode = possiblePaths.pop(0)
        pathsTotake.remove(currentNode.location)
        traveledPaths.append(currentNode)
        print(str(currentNode.location))


    numberOfSteps = 0
    while(currentNode.parent!=None):
        currentNode = currentNode.parent
        numberOfSteps+=1

    print(numberOfSteps)
    pass

def main():
    solve(
        [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]],
        (3,0),
        (0,0)
    )
    pass

if __name__ == "__main__":
    main()