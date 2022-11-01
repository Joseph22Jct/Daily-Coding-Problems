# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall 
# and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index 
# (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

def solve(bucketList):
    answer = [0 for i in range(len(bucketList))]
    bl = (list(enumerate(bucketList)))
    BucketWallL = bl[0]
    BucketWallR = None

    for no,Val in bl:
        
        if(no == 0):
            pass
        elif(BucketWallL[1] > Val or no >= len(bl)):
           
            if (BucketWallR == None):
                BucketWallR = (no,Val)
            elif(BucketWallR[1]<=Val):
                BucketWallR = (no,Val)
            #print(str(BucketWallR))
        else:
            #print("works")
            if(BucketWallR[1]<=Val):
                BucketWallR = (no,Val)
            
            lowestWall = BucketWallL
            if(lowestWall[1]>BucketWallR[1]):
                lowestWall = BucketWallR
            #print(str(BucketWallL) + str(BucketWallR))
            for x in range(BucketWallL[0],BucketWallR[0]):
                if (x!= BucketWallL[0] or x!= BucketWallR[0]):
                    answer[x] = lowestWall[1]-bl[x][1]
                else:
                    answer[x] = 0
            BucketWallL = (no,Val)
    return answer

def main():
    bL1 = [2, 1, 2]
    bL2 = [3, 0, 1, 3, 0, 5]
    bL2R = [5,0,3,1,0,3]
    print(str(solve(bL1)))
    print(str(solve(bL2)))
    #print(str(solve(bL2R)))
    pass

if __name__ == "__main__":
    main()